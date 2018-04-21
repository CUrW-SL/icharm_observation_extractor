#!/usr/bin/env bash

cd /home/uwcc-admin/icharm_observation_extractor/
source venv/bin/activate
python extractor.py >> logs/icharm_extractor.log
deactivate