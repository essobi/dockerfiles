FROM node:6  
WORKDIR /opt/trambar  
  
# install ffmpeg  
RUN echo "deb http://ftp.uk.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list.d/backports.list  
RUN apt-get -y update && apt-get -y install ffmpeg  
  
# install dependencies  
COPY package.json backend/  
RUN cd backend && npm install  
  
# copy codebase  
COPY common common/  
COPY backend backend/  
  
WORKDIR /opt/trambar/backend/src  

