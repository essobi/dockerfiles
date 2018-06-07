FROM dimdm/node:8.9.0  
ENV NODE_ENV=production  
ARG NODE_ENV=production  
ARG RADAPI_PATH=/radapi  
  
COPY package.json yarn.lock .bowerrc bower.json index.js ${RADAPI_PATH}/  
COPY public/* ${RADAPI_PATH}/public/  
ADD https://raw.githubusercontent.com/node-
red/catalogue.nodered.org/master/catalogue.json ${RADAPI_PATH}/public/  
  
WORKDIR ${RADAPI_PATH}  
RUN apk --no-cache add --virtual build-dependencies \  
git \  
build-base \  
python \  
yarn &&\  
mkdir -p ${RADAPI_PATH}/data &&\  
cd ${RADAPI_PATH} &&\  
yarn add bower &&\  
yarn &&\  
yarn remove bower &&\  
apk del --purge build-dependencies &&\  
rm -rf /var/cache/apk/* &&\  
rm -rf /root/* &&\  
rm -rf /tmp/* &&\  
addgroup -g 1000 radapi &&\  
adduser -D -u 1000 -G radapi radapi &&\  
chown -R radapi:radapi ${RADAPI_PATH}  
  
VOLUME ${RADAPI_PATH}/data  
VOLUME ${RADAPI_PATH}/public  
  
EXPOSE 1880  
USER radapi  
  
CMD npm start  

