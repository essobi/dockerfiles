FROM node  
RUN npm install -g amazon-elasticsearch-proxy && \  
sed -i 's/127.0.0.1/0.0.0.0/g' /usr/local/lib/node_modules/amazon-
elasticsearch-proxy/cli.js  
EXPOSE 9200  

