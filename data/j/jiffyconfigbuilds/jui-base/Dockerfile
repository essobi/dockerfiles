FROM node:6  
MAINTAINER Thomas Chan "workingtheory@thytruth.com"  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app  
RUN npm set progress=false \  
&& npm cache clean \  
&& npm install --registry http://registry.npmjs.org \  
&& npm config set registry https://registry.npmjs.org/ \  
&& npm install  

