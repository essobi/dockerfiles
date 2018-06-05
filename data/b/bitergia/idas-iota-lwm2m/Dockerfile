FROM node:0.10-slim  
  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV IOTA_PATH /opt/iotagent-lwm2m  
ENV IOTA_LOG_PATH /var/log/iotagent-lwm2m  
ENV GIT_IOTA_VERSION 0.2.0  
ENV IOTA_USER iota  
  
COPY config.js /opt/config.js  
  
RUN adduser --disabled-password --gecos "${IOTA_USER}" ${IOTA_USER}  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends git ca-certificates netcat curl gcc
g++ make python && \  
git clone https://github.com/telefonicaid/lightweightm2m-iotagent.git
${IOTA_PATH} && \  
cd ${IOTA_PATH} && \  
git checkout ${GIT_IOTA_VERSION} && \  
npm install --production && \  
npm install forever --global && \  
npm cache clear && \  
mv /opt/config.js ${IOTA_PATH}/config.js && \  
chown -R ${IOTA_USER}:${IOTA_USER} ${IOTA_PATH} && \  
apt-get -y purge python g++ gcc make && \  
apt-get -y autoremove --purge && \  
apt-get clean && \  
find /var/lib/apt/lists -type f -delete && \  
rm -rf /root/.npm /root/.node-gyp  
  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
### Exposed ports  
# - IoT Agent  
EXPOSE 4041  

