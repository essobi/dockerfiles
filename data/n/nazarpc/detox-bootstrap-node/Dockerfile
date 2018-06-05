FROM node:10  
LABEL maintainer="Nazar Mokrynskyi <nazar@mokrynskyi.com>"  
  
COPY bin/detox-bootstrap-node.js /code/bin/detox-bootstrap-node  
COPY src/index.js /code/src/index.js  
COPY package.json /code  
  
WORKDIR /code  
  
RUN npm install --production  
  
EXPOSE 16882/tcp  
  
ENTRYPOINT ["bin/detox-bootstrap-node"]  

