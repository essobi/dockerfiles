FROM jeffutter/iojs-xvfb-chromium  
MAINTAINER jeff@jeffutter.com  
  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD RUN npm install  
ONBUILD COPY . /usr/src/app  
  
CMD npm test  

