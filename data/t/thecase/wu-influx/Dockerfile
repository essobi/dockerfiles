FROM alpine:latest  
  
RUN apk add --update python py-pip  
RUN pip install --upgrade pip  
  
RUN pip install influxdb  
  
COPY wu-influx.py /  
  
ENV INFLUXHOST localhost  
ENV INFLUXPORT 8086  
ENV INFLUXUSER root  
ENV INFLUXPASS root  
ENV INFLUXDB wu  
  
# time between API hits< in seconds  
ENV POLL_INTERVAL 600  
ENV WU_KEY XXXXXXXXXX  
ENV WU_CITY Bozeman  
ENV WU_STATE MT  
  
CMD [ "python", "wu-influx.py" ]  

