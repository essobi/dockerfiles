FROM node:0.10.36  
WORKDIR /opt/app  
  
VOLUME ["/opt/app/db"]  
EXPOSE 2012  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install --production && cp -R node_modules /opt/app  
  
ADD . /opt/app  
  
CMD ["bin/server"]  

