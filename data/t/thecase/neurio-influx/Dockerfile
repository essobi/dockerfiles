FROM alpine:latest  
  
RUN apk add --update python py-pip  
RUN pip install --upgrade pip  
  
RUN pip install neurio influxdb  
  
COPY *.py /  
  
ENV INFLUXHOST localhost  
ENV INFLUXPORT 8086  
ENV INFLUXUSER root  
ENV INFLUXPASS root  
ENV INFLUXDB neurio  
  
# time between API hits in seconds  
ENV POLL_INTERVAL 60  
ENV N_SENSOR XXXXXXXXXXXX  
ENV N_KEY 111111111111  
ENV N_SECRET 000000000000  
CMD [ "python", "neurio-influx.py" ]  

