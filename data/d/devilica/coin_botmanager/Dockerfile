FROM node:6.12.0-slim  
  
MAINTAINER KwonYoung Kim <kykim79@gmail.com>  
  
ENV TZ Asia/Seoul  
  
RUN echo "${TZ}" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
&& mkdir -p /app  
  
COPY package.json /app  
  
RUN cd /app; npm install  
  
WORKDIR /app  
  
ADD . /app  
  
VOLUME [ "/app/config", "/app/log" ]  
  
CMD node botManager.js  

