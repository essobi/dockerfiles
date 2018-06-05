FROM node:6-alpine  
RUN apk add --update jq bash && rm -rf /var/cache/apk/*  
RUN npm i -g csv2json csvtojson jsonlint fast-csv j xml2json-command generate-
schema  
WORKDIR /data  
USER node  

