FROM grafana/grafana:5.0.4  
RUN apt-get update && apt-get install -y netcat mysql-client  
  
COPY ./start.sh /bin/start.sh  
  
ENTRYPOINT []  
CMD /bin/bash /bin/start.sh  

