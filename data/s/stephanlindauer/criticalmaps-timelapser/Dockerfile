FROM node:6.4  
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list && \  
apt-get -qq update && \  
apt-get -qq -y install ffmpeg  
  
RUN groupadd -r node && useradd -r -g node node  
  
ENV APP_DIR /usr/src/app/  
  
RUN mkdir -p $APP_DIR  
WORKDIR $APP_DIR  
  
COPY package.json $APP_DIR  
RUN npm install --silent  
  
COPY . $APP_DIR  
  
RUN chown -R node:node $APP_DIR  
  
CMD [ "npm", "start" ]  

