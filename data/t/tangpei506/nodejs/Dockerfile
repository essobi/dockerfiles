FROM debian:jessie  
  
# Update packages  
RUN apt-get update && apt-get -y upgrade  
  
# install nodejs via package manager  
RUN apt-get install -y build-essential libssl-dev curl sudo bash \  
&& curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# Install dep for node-canvas  
RUN apt-get install -y libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev
libgif-dev build-essential g++  
  
#deps for static data  
RUN apt-get update && \  
apt-get install -y git python libav-tools python3 python3-pip default-jre
sqlite3 && \  
apt-get clean  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD RUN npm install  
ONBUILD COPY . /usr/src/app  
  
EXPOSE 8000  
CMD [ "npm", "start" ]  

