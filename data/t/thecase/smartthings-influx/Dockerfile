FROM alpine:latest  
  
RUN apk add --update python py-pip  
RUN pip install --upgrade pip  
  
RUN pip install requests influxdb  
  
COPY *.py /  
  
ENV INFLUXHOST localhost  
ENV INFLUXPORT 8086  
ENV INFLUXUSER root  
ENV INFLUXPASS root  
ENV INFLUXDB zwave  
  
# time between API hits in seconds  
ENV POLL_INTERVAL 300  
ENV ST_TOKEN XXXXXXXXXXXX  
  
CMD [ "python", "smartthings.py" ]  

