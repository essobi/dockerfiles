FROM node:7.5  
EXPOSE 80  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
  
RUN npm install --global nodemon babel-core babel-cli  
RUN npm install  
COPY . /usr/src/app  
  
LABEL traefik.backend=party_party_service  
LABEL traefik.frontend.rule=Host:localhost;PathPrefixStrip:/api/party  
LABEL traefik.port=80  
LABEL traefik.frontend.entryPoints=http  
  
CMD [ "nodemon", "index.js", "--exec", "babel-node"]  

