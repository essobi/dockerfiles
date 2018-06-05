FROM ucalgary/python-librdkafka  
  
RUN apk add --update --no-cache git gcc musl-dev  
  
RUN mkdir -p /var/modulo12/boltz-raspberry  
  
WORKDIR /var/modulo12/boltz-raspberry  
  
ADD . /var/modulo12/boltz-raspberry  
  
COPY start.sh /var/modulo12/boltz-raspberry  
  
RUN chmod +x /var/modulo12/boltz-raspberry/start.sh  
  
RUN pip install confluent_kafka confluent-kafka[avro] requests avro-python3  
  
CMD ["/var/modulo12/boltz-raspberry/start.sh"]  

