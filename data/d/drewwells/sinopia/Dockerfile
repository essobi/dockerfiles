FROM google/nodejs:0.10.33  
MAINTAINER Drew Wells <drew.wells00@gmail.com>  
  
VOLUME /opt/sinopia/storage  
VOLUME /etc/sinopia  
WORKDIR /opt/sinopia  
RUN npm install --verbose sinopia@1.0.0-alpha.3  
  
EXPOSE 4873  
CMD ["node", "/opt/sinopia/node_modules/sinopia/bin/sinopia", "--config",
"/etc/sinopia/config.yaml"]  

