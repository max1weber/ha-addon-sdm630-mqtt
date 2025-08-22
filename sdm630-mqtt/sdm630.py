import os
import time
import struct
import json
from pymodbus.client import ModbusTcpClient
import paho.mqtt.publish as publish

def read_float(client, reg, slave_id):
    rr = client.read_input_registers(reg, 2, unit=slave_id)
    if rr.isError():
        return None
    val = (rr.registers[0] << 16) + rr.registers[1]
    return struct.unpack('>f', val.to_bytes(4, 'big'))[0]

def main():
    usr_ip = os.getenv("USR_IP", "192.168.1.100")
    usr_port = int(os.getenv("USR_PORT", "502"))
    slave_id = int(os.getenv("SLAVE_ID", "1"))
    mqtt_broker = os.getenv("MQTT_BROKER", "core-mosquitto")
    mqtt_port = int(os.getenv("MQTT_PORT", "1883"))
    mqtt_topic = os.getenv("MQTT_TOPIC", "home/sdm630")

    client = ModbusTcpClient(usr_ip, port=usr_port)

    while True:
        try:
            if not client.connect():
                print("❌ Kan geen verbinding maken met Modbus TCP")
                time.sleep(5)
                continue

            data = {
                "voltage_l1": read_float(client, 0, slave_id),
                "voltage_l2": read_float(client, 2, slave_id),
                "voltage_l3": read_float(client, 4, slave_id),
                "current_l1": read_float(client, 6, slave_id),
                "current_l2": read_float(client, 8, slave_id),
                "current_l3": read_float(client, 10, slave_id),
                "power_total": read_float(client, 52, slave_id),
                "energy_import": read_float(client, 72, slave_id),
                "energy_export": read_float(client, 74, slave_id)
            }

            publish.single(mqtt_topic, json.dumps(data), hostname=mqtt_broker, port=mqtt_port)
            print("✅ Data gepubliceerd:", data)

        except Exception as e:
            print("⚠️ Fout:", e)

        time.sleep(10)

if __name__ == "__main__":
    main()
