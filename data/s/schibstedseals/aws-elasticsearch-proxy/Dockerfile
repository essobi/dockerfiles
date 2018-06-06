FROM node:6.3  
WORKDIR /proxy  
RUN npm install aws-sdk http-proxy express body-parser  
ADD es_proxy.js /proxy/es_proxy.js  
EXPOSE 9900  
CMD node es_proxy.js

