FROM node:latest  
  
ENV NODE_ENV production  
RUN mkdir -p /usr/src/client \  
&& git clone https://github.com/siggame/Joueur.js.git /usr/src/assets \  
&& cp /usr/src/assets/package.json /usr/src/client \  
&& cd /usr/src/client \  
&& npm install && npm cache clean --force  
WORKDIR /usr/src/client  
  
ONBUILD COPY package.json .  
ONBUILD RUN npm install && npm cache clean --force  
  
ONBUILD COPY . /usr/src/client  

