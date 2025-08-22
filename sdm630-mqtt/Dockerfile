FROM python:3.11-slim

WORKDIR /app

RUN pip install pymodbus==3.6.9 paho-mqtt==2.1.0

COPY sdm630.py run.sh /app/

RUN chmod +x /app/run.sh

CMD ["/app/run.sh"]