FROM mhart/alpine-node:5  
ADD package.json /tmp/package.json  
RUN cd /tmp \  
&& npm install --production \  
&& mkdir -p /opt/app \  
&& cp -a /tmp/node_modules /opt/app/  
  
WORKDIR /opt/app  
ADD ./ /opt/app  
  
EXPOSE 8081  
CMD node server.js  

