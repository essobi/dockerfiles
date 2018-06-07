FROM alpine:3.5  
MAINTAINER DUONG Dinh Cuong <cuong3ihut@gmail.com>  
  
COPY . /data  
WORKDIR /data  
VOLUME /root/.aws/  
RUN chmod +x ./app-deploy  
  
# bower requires this configuration parameter to allow bower install using
root.  
RUN echo '{ "allow_root": true }'>.bowerrc  
  
# node-sass doesn't support Alpine, so we need the build toolchain.  
RUN apk --update add curl git ca-certificates openssh-client python build-base
nodejs &&\  
mkdir /root/.ssh/ && cp /data/ssh/id_rsa /root/.ssh/id_rsa && chmod 600
/root/.ssh/id_rsa && touch /root/.ssh/known_hosts && ssh-keyscan bitbucket.org
>> /root/.ssh/known_hosts &&\  
./app-deploy "R1" "YES" "sensor-remote-dashboard" "/root" &&\  
npm install -g --unsafe-perm node-red &&\  
cd /root/.node-red/ && npm install node-red-contrib-http-auth0 && npm install
node-red-contrib-aws-sdk && npm install node-red-contrib-func-exec && npm
install node-red-contrib-job-queue &&\  
apk del ca-certificates git python build-base &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -rf /var/cache/apk/* &&\  
cp /data/flows/settings.js /root/.node-red/settings.js &&\  
cp /data/flows/flows.json /root/.node-red/flows.json &&\  
rm -rf /data  
  
EXPOSE 1880  
ENTRYPOINT ["node"]  
CMD ["/usr/bin/node-red"]  

