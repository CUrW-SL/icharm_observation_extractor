import pandas as pd
import copy
from datetime import datetime

from curwmysqladapter import MySQLAdapter, Station, Data

from config import Common_DateTime_Format, DB_CONFIG, Links, get_station_info


timeseries_meta_struct = {
    'station': '',
    'variable': '',
    'unit': '',
    'type': '',
    'source': '',
    'name': ''
}


def build_timestamp(data_array):
    timestamp = datetime(year=data_array[0], month=data_array[1], day=data_array[2], hour=data_array[3])
    return timestamp.strftime(Common_DateTime_Format)


def prepare_timeseries(df):
    timeseries = []
    for index, row in df.iterrows():
        timeseries.append([row['timestamp'], row['value']])
    return timeseries


# Create database connections.
mysql_adapter = MySQLAdapter(host=DB_CONFIG['MYSQL_HOST'], user=DB_CONFIG['MYSQL_USER'],
                                 password=DB_CONFIG['MYSQL_PASSWORD'], db=DB_CONFIG['MYSQL_DB'])

print('\n##########################################################################################')
print("Extracting Observed data from Icharm on %s" % datetime.now().strftime(Common_DateTime_Format))

# Iterate over Icharm csv file download links and push date to DB
for station_id, url in Links.items():
    # Load the .csv to a Dataframe
    df = pd.read_csv(url, header=None, names=['year', 'month', 'day', 'hour', 'value'])
    df['timestamp'] = df[['year', 'month', 'day', 'hour']].apply(build_timestamp, raw=True, axis=1)

    # IF station does not exist in the database create one with given station configs details.
    station_info = get_station_info(station_id)
    station_details_in_db = mysql_adapter.get_station(
        {'stationId': station_info['stationId'], 'name': station_info['name']})
    if station_details_in_db is None:
        print("Station: {stationId: %s, name: %s} does not exist in the DB. Creating station in the DB..."
              % (station_info['stationId'], station_info['name']))
        station_meta_list = station_info['station_meta']
        station_meta_list.insert(0, Station.CUrW)
        row_count = mysql_adapter.create_station(station_meta_list)
        if row_count > 0:
            print("Created new station: ", station_meta_list)
        else:
            print("Unable to create new station: ", station_meta_list)
            continue

    # Create event metadata. Event metadata is used to create timeseries id (event_id) for the timeseries.
    timeseries_meta = copy.deepcopy(timeseries_meta_struct)
    timeseries_meta['station'] = station_info['name']
    timeseries_meta['variable'] = 'Precipitation'
    timeseries_meta['unit'] = 'mm'
    timeseries_meta['type'] = station_info['type']
    timeseries_meta['source'] = station_info['source']
    timeseries_meta['name'] = station_info['run_name']

    # At this point station exists. Check whether there is a timeseries_id (or event-id).
    # If does not exist create an id.
    timeseries_id = mysql_adapter.get_event_id(timeseries_meta)
    if timeseries_id is None:
        print("No timeseries for the '%s' of the station: %s in the DB. Creating timeseries-id..."
              % (timeseries_meta['variable'], station_info['stationId'] + '/' + station_info['name']))
        timeseries_id = mysql_adapter.create_event_id(timeseries_meta)

    timeseries = prepare_timeseries(df)

    # Insert timeseries.
    print("Pushing to timeseries: %s of size %d" % (timeseries_id, len(timeseries)))
    inserted_rows = mysql_adapter.insert_timeseries(timeseries_id, timeseries, True, Data.data)
    print("Inserted %d rows from %d timeseries_id values successfully..." % (inserted_rows, len(timeseries)))

