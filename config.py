Common_DateTime_Format = '%Y-%m-%d %H:%M:%S'

DB_CONFIG = {
    'MYSQL_HOST': "",
    'MYSQL_USER': "",
    'MYSQL_PASSWORD': "",
    'MYSQL_DB': "curw"
}

Links = {'icharm_kalutara': 'http://ff-srilanka.diasjp.net/insitu/KALU01_A_Kalutara_10days_hr.csv',
         'icharm_kalawana': 'http://ff-srilanka.diasjp.net/insitu/KALU02_B_Kalawana_10days_hr.csv',
         'icharm_ratnapura': 'http://ff-srilanka.diasjp.net/insitu/KALU03_C_Ratnapra_10days_hr.csv',
         'icharm_kahawatta': 'http://ff-srilanka.diasjp.net/insitu/KALU04_D_Kahawatta_10days_hr.csv',
         'icharm_dompe': 'http://ff-srilanka.diasjp.net/insitu/KALU05_E_Doampe_10days_hr.csv',
         'icharm_colombo': 'http://ff-srilanka.diasjp.net/insitu/KALU06_F_Colombo_10days_hr.csv',
         'icharm_hirase': 'http://ff-srilanka.diasjp.net/insitu/KALU07_G_Hirase_10days_hr.csv',
         'icharm_neluwa': 'http://ff-srilanka.diasjp.net/insitu/KALU08_H_Neluwa_10days_hr.csv',
         'icharm_akurassa': 'http://ff-srilanka.diasjp.net/insitu/KALU09_I_Akurassa_10days_hr.csv'
         }

StationConfigs = [{
            "stationId": "icharm_kalutara",
            "name": "Kalutara",
            "station_meta": ["icharm_kalutara", "Kalutara", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_kalawana",
            "name": "Kalawana",
            "station_meta": ["icharm_kalawana", "Kalawana", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_ratnapura",
            "name": "Ratnapura",
            "station_meta": ["icharm_ratnapura", "Ratnapura", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_kahawatta",
            "name": "Kahawatta",
            "station_meta": ["icharm_kahawatta", "Kahawatta", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_dompe",
            "name": "Dompe",
            "station_meta": ["icharm_dompe", "Dompe", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_colombo",
            "name": "Colombo",
            "station_meta": ["icharm_colombo", "Colombo", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_hirase",
            "name": "Hirase",
            "station_meta": ["icharm_hirase", "Hirase", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_neluwa",
            "name": "Neluwa",
            "station_meta": ["icharm_neluwa", "Neluwa", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }, {
            "stationId": "icharm_akurassa",
            "name": "Akurassa",
            "station_meta": ["icharm_akurassa", "Akurassa", 0, 0, 0, "Observed data from Icharm"],
            "source": "WeatherStation",
            "type": "Observed",
            "variables": ["Precipitation"],
            "units": ["mm"],
            "max_values": ["120"],
            "min_values": ["0"],
            "description": "Observed data from Icharm",
            "run_name": "Icharm"
        }]


def get_station_info(station_id):
    for station in StationConfigs:
        if station['stationId'] == station_id:
            return station
    return None
