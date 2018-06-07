FROM mhart/alpine-node:6.1  
RUN apk update  
RUN apk add git  
  
RUN mkdir -p /opt/app  
WORKDIR /opt/app  
ADD ./package.json /opt/app/package.json  
RUN npm install  
ADD ./start.js /opt/app/start.js  
  
CMD ["node", "start.js"]  

