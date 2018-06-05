FROM node:alpine  
  
MAINTAINER Dmitry Karikh <the.dr.hax@gmail.com>  
  
RUN apk --no-cache add git \  
&& git clone https://github.com/maxsivanov/influxdb-timeshift-proxy.git \  
&& cd influxdb-timeshift-proxy \  
&& npm i  
  
ENV INFLUXDB=influxdb:8086  
EXPOSE 8089  
WORKDIR influxdb-timeshift-proxy  
  
CMD npm run start  

