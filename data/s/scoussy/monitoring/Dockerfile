FROM scoussy/node-red:alpine  
  
RUN apk -U add tcpdump  
  
RUN npm install --prefix /root/.node-red/ dockerode fast-json-patch read-file  
  
COPY root /root  
COPY flows.json /flows.json  
COPY config.default /config.default  

