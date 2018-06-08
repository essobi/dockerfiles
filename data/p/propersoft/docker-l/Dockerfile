FROM mhart/alpine-node:latest  
  
MAINTAINER Alpha Hinex <AlphaHinex@gmail.com>  
  
RUN apk add --no-cache tzdata  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN apk del tzdata  
  
# RUN apt-get -q update  
# RUN apt-get -qy install git-core redis-server  
RUN apk add --no-cache make g++ python git supervisor  
  
WORKDIR /home  
RUN git clone https://github.com/propersoft-cn/L.git  
  
WORKDIR /home/L  
RUN npm install  
  
COPY l.conf /etc/supervisor/conf.d/l.conf  
CMD supervisord -c /etc/supervisor/conf.d/l.conf  

