FROM node:6.9.1  
RUN apt-get update && apt-get install -y libcairo2-dev libjpeg62-turbo-dev
libpango1.0-dev libgif-dev build-essential g++  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENV NODE_ENV $NODE_ENV  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
RUN mkdir -p /usr/src/app/public/images  
RUN cd /usr/src/app/public/js && npm install  
  
EXPOSE 3055  
CMD [ "npm", "start" ]  

