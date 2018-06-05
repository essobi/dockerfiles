FROM cuongdd1/seniot-gateway:latest  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
COPY . /data  
COPY settings.js /root/.node-red/  
COPY flows.json /usr/share/.node-red/  
  
RUN cd /data/nodes/sensor-analytics/ && npm install && mv /data/nodes
/usr/share/.node-red/ &&\  
cd /root/seniot-gateway && npm install node-red-contrib-http-auth0  
  
EXPOSE 1880  
ENTRYPOINT ["node"]  
CMD ["/root/seniot-gateway/red", "--harmony"]

