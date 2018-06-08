FROM node:6-slim  
  
RUN apt-get update && apt-get install -y bzip2 libfontconfig  
  
WORKDIR /opt/app  
  
ADD package.json /opt/app/  
  
RUN npm install && npm install -g phantomjs-prebuilt  
  
ADD . /opt/app/  
  
ENTRYPOINT ["node", "src/index.js"]  

