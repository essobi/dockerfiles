FROM node:7.5  
MAINTAINER marley (www.marley.org)  
  
WORKDIR /src  
  
ADD package.json /src/  
RUN npm install  
ADD . /src/  
  
EXPOSE 3000  
CMD /usr/local/bin/nodejs /src/app.js  

