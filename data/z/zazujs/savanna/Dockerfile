FROM mhart/alpine-node:5  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
ADD . /opt/app  
  
EXPOSE 1337  
CMD ["node", "app.js"]  

