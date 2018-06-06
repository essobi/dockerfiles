FROM cuongdd1/citus-iot-ecosystem-website:base  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
COPY . /data  
WORKDIR /data  
VOLUME /root/.kube/  
RUN mkdir -p /root/.yaml/  
RUN chmod +x ./app-deploy  
  
# bower requires this configuration parameter to allow bower install using
root.  
RUN echo '{ "allow_root": true }'>.bowerrc  
  
# node-sass doesn't support Alpine, so we need the build toolchain.  
RUN cd /data/ && ./app-deploy "R1" "YES" "citus-iot-ecosystem-website" "/root"
&&\  
cp /data/flows/settings.js /root/.node-red/settings.js &&\  
cp /data/flows/flows.json /root/.node-red/flows.json &&\  
cp /data/scripts/rolling-update-kubernetes-service /usr/sbin/ &&\  
cp /data/scripts/change-default-quota-limit /usr/sbin/ &&\  
cp /data/scripts/delete-application-by-namespace /usr/sbin/ &&\  
cp /data/patterns/compute-resources.yaml /root/.yaml/ &&\  
chmod +x /usr/sbin/rolling-update-kubernetes-service &&\  
chmod +x /usr/sbin/change-default-quota-limit &&\  
chmod +x /usr/sbin/delete-application-by-namespace &&\  
apk del ca-certificates git python build-base &&\  
rm -rf /data  
  
EXPOSE 1880  
ENTRYPOINT ["node"]  
CMD ["/usr/bin/node-red"]  
  

