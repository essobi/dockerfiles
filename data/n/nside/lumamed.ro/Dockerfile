# nodejs static site  
FROM node:4-onbuild  
MAINTAINER bogdan.nenu@gmail.com  
  
# Bundle app source  
COPY package.json /src/  
# Install app dependencies  
RUN cd /src; npm install  
  
# Copy distro  
COPY ./app /src/app/  
COPY ./test /src/test/  
COPY main.js /src/  
  
EXPOSE 3000  
CMD cd /src && node main.js  

