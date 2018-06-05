FROM ubuntu:16.04 as base  
  
# Install dependencies  
RUN apt-get update --yes && apt-get upgrade \--yes && apt-get install git
nodejs npm \  
libcairo2-dev libjpeg8-dev libpango1.0-dev libgif-dev libpng-dev build-
essential g++ \  
ffmpeg \  
redis-server --yes && ln -s `which nodejs` /usr/bin/node  
  
WORKDIR /audiogram  
COPY package.json package.json  
RUN npm i  
  
COPY . .  
  
RUN npm run build  
  
CMD [ "npm", "start" ]

