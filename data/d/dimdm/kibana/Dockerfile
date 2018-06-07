FROM dimdm/node:6.11.1  
ARG KIBANA_VERSION=5.4.0  
ARG KIBANA_PATH=/kibana  
ENV NODE_ENV=production  
  
RUN apk --no-cache add --virtual build-dependencies \  
build-base \  
python \  
git &&\  
git clone \--depth 1 --branch v${KIBANA_VERSION}
https://github.com/ddm/kibana.git ${KIBANA_PATH} &&\  
cd ${KIBANA_PATH} &&\  
npm install &&\  
apk del --purge build-dependencies &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /root/* &&\  
rm -rf /tmp/* &&\  
adduser -D -u 1000 kibana &&\  
mkdir -p ${KIBANA_PATH}/config/ &&\  
chown -R kibana:kibana ${KIBANA_PATH}  
  
COPY kibana.yml ${KIBANA_PATH}/config/kibana.yml  
  
USER kibana  
WORKDIR ${KIBANA_PATH}  
CMD /kibana/bin/kibana -p 5601 -e http://elasticsearch:9200/ -c
/kibana/config/kibana.yml  

