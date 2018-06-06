# Pulling nodejs base image  
FROM node:0.12  
# Skip npm install if package.json didn't changed  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install --production  
RUN mkdir -p /opt/status-checker && cp -a /tmp/node_modules /opt/status-
checker  
  
# Loading application code  
WORKDIR /opt/status-checker  
ADD . /opt/status-checker  
  
# Expose API port  
EXPOSE 9090  
CMD ["node", "."]  

