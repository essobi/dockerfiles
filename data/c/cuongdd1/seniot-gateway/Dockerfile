FROM alpine:3.5  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
RUN mkdir -p /usr/local/.node-red  
COPY lib/flows/settings.js /root/.node-red/  
COPY app-deploy /data/  
VOLUME /usr/local/.node-red  
  
RUN chmod +x /data/app-deploy  
  
ENV DEVICE_ID= SECRET_KEY= SELF_ACTIVATION=NO INSTALL_DOCKER=NO  
  
# bower requires this configuration parameter to allow bower install using
root.  
RUN echo '{ "allow_root": true }'>.bowerrc  
  
# node-sass doesn't support Alpine, so we need the build toolchain.  
RUN apk --update add curl git ca-certificates python build-base nodejs &&\  
rm -rf $HOME/citus-iot-device-agents/ &&\  
cd /data/ && ./app-deploy "R1" "YES" "seniot-gateway" "/root" &&\  
cd /root/seniot-gateway/ && npm install node-red-dashboard && npm install
node-red-contrib-http-auth0 && npm install node-red-contrib-aws-sdk && npm
install node-red-contrib-azure-https && npm install node-red-contrib-func-exec
&& npm install node-red-contrib-aws-iot-hub &&\  
apk update && apk add ca-certificates wget && update-ca-certificates &&\  
apk del build-base python curl &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /var/cache/apk/* &&\  
mkdir -p /root/.node-red/ &&\  
rm -rf /data  
  
EXPOSE 1880  
ENTRYPOINT ["node"]  
CMD ["/root/seniot-gateway/red", "--harmony"]  
  

