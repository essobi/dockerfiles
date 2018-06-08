FROM python:2  
ENV OBSERVER_MQTT_HOST 192.168.1.1 \  
OBSERVER_MQTT_PORT 1883 \  
OBSERVER_MQTT_ENTRYPOINT /test/meteo \  
OBSERVER_HOST 192.168.1.10  
RUN mkdir /app && chown nobody /app  
VOLUME ["/app"]  
WORKDIR /app  
ADD requirements.txt /app  
RUN pip install -r requirements.txt  
USER nobody  
ADD observerip.py /app  
CMD [ "python", "/app/observerip.py" ]  

