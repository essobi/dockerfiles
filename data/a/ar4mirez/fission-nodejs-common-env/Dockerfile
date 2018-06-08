FROM node:8-onbuild  
RUN npm i -g npm  
  
ONBUILD RUN curl -o package.json
https://gist.githubusercontent.com/ar4mirez/e53472390fb9e8e20fe292d861198969/raw/87d0e8ee3bed482284bdcf4e558cd700107aed24/package.json
&& \  
mv package.json /usr/src/app/package.json  
  
ADD package.json /usr/src/app/package.json  
  
ONBUILD RUN npm i --production --silent  
  
ADD server.js /usr/src/app/server.js  
  
EXPOSE 8888  

