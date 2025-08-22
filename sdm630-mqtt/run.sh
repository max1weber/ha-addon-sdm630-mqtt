#!/usr/bin/with-contenv bashio
set -e

# Lees opties en exporteer als environment variables
export USR_IP=$(bashio::config 'usr_ip')
export USR_PORT=$(bashio::config 'usr_port')
export SLAVE_ID=$(bashio::config 'slave_id')
export MQTT_BROKER=$(bashio::config 'mqtt_broker')
export MQTT_PORT=$(bashio::config 'mqtt_port')
export MQTT_TOPIC=$(bashio::config 'mqtt_topic')

python3 /app/sdm630.py
