FROM node:9  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libcairo2-dev \  
libjpeg-dev \  
libpango1.0-dev \  
libgif-dev \  
build-essential \  
g++  
  
WORKDIR /usr/src/app  
  
COPY config ./config  
COPY fonts ./fonts  
COPY lib ./lib  
COPY index.js ./index.js  
COPY package.json ./package.json  
  
RUN npm install  
  
EXPOSE 3001  
CMD [ "npm", "run", "start" ]

