FROM node:9.4.0  
  
RUN set -ex ; \  
apt update ; \  
apt install git python make g++ ; \  
mkdir -p /opt/node-open-mining-portal  
  
COPY package.json /opt/node-open-mining-portal/  
  
WORKDIR /opt/node-open-mining-portal  
  
RUN npm update  
  
COPY . /opt/node-open-mining-portal/  
  
RUN rm -rf /opt/node-open-mining-portal/pool_configs  
RUN ln -s /opt/config/config.json /opt/node-open-mining-portal/config.json  
RUN ln -s /opt/config/pool_configs /opt/node-open-mining-portal/  
  
VOLUME ["/opt/config"]  
  
EXPOSE 80  
EXPOSE 3333  
  
CMD node init.js

