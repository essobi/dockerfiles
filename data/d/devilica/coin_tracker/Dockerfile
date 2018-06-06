FROM node:6.12.0-slim  
  
MAINTAINER KwonYoung Kim <kykim79@gmail.com>  
  
ENV TZ Asia/Seoul  
  
RUN echo "${TZ}" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
&& mkdir -p /app  
  
COPY package.json /app  
  
RUN cd /app; npm install  
  
WORKDIR /app  
  
ADD . /app  
  
RUN mkdir -p /app/config  
  
RUN mkdir -p /app/chartData  
  
VOLUME [ "/app/config", "/app/chartData", "/app/log" ]  
  
CMD node tracker.js  

