FROM alpine:latest  
  
RUN apk add --update python py-pip  
RUN pip install --upgrade pip  
  
RUN mkdir /opt  
COPY files /opt  
  
RUN cd /opt && pip install xmltodict influxdb incremental constantly  
RUN apk add py-twisted  
  
ENV INFLUXHOST localhost  
ENV INFLUXPORT 8086  
ENV INFLUXUSER admin  
ENV INFLUXPASS admin  
ENV INFLUXDB bryant  
  
EXPOSE 8080  
CMD [ "python", "/opt/proxy.py" ]  

