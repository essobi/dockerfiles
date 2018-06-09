FROM node:4.7.3-alpine  
  
RUN apk update && \  
apk upgrade && \  
apk add git  
  
RUN npm install jspm@beta -g  
  
ADD . /src/  
WORKDIR /src/  
  
RUN npm install && jspm install && jspm bundle browser.js build.js --minify  
  
CMD jspm run server.js  
EXPOSE 80  

