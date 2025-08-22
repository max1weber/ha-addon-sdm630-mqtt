# SDM630 Modbus → MQTT Bridge (Home Assistant Add-on)

Deze add-on leest een **Eastron SDM630 kWh-meter** via een **USR-TCP232-410S (RS485 ↔ Ethernet)** 
en publiceert de data naar een MQTT broker (bij voorkeur de Home Assistant core-mosquitto add-on).

## Installatie
1. Voeg deze repository toe in Home Assistant → Add-on store → Repositories.
2. Installeer **SDM630 MQTT Bridge**.
3. Configureer het IP-adres en de instellingen van de USR-TCP232-410S.
4. Start de add-on → meetdata verschijnt in MQTT.

## MQTT topic voorbeeld
```json
{
  "voltage_l1": 229.4,
  "voltage_l2": 228.9,
  "voltage_l3": 230.1,
  "current_l1": 1.23,
  "current_l2": 0.87,
  "current_l3": 1.05,
  "power_total": 1500.2,
  "energy_import": 12345.6,
  "energy_export": 234.5
}
