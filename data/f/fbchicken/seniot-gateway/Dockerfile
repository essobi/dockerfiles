FROM cuongdd1/seniot-gateway:latest  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
COPY . /data  
COPY settings.js /root/.node-red/  
COPY flows.json /usr/share/.node-red/  
COPY certs /root/.agent/certs  
  
RUN cd /data/nodes/mqtt-singleton/ && npm install  
RUN cd /data/nodes/citus-sensors/ && npm install && mv /data/nodes
/usr/share/.node-red/  
  
EXPOSE 1880  
ENTRYPOINT ["node"]  
CMD ["/root/seniot-gateway/red", "--harmony"]

