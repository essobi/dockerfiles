FROM node:4-onbuild  
MAINTAINER Fabio Sforza <fabio.sforza@relatech.com>  
  
COPY package.json /src/package.json  
COPY helloworld.js /src/helloworld.js  
  
CMD ["node", "/src/helloworld.js"]  
  
VOLUME ["/log"]  
  
EXPOSE 1337  

