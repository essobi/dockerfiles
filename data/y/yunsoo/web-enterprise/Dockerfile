FROM nginx:latest  
MAINTAINER Lijian Qiu <lijian@yunsu.co>  
  
RUN apt-get update && \  
apt-get install -yq zip curl && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/yunsoo && \  
curl -o /var/yunsoo/dev.zip -L
https://github.com/dataDeathKnight/yunsoo/archive/dev.zip && \  
cd /var/yunsoo && unzip dev.zip && mv yunsoo-dev/* . && rm -rf yunsoo-dev
dev.zip && \  
rm -rf /usr/share/nginx/html/* && \  
cp -r /var/yunsoo/web-enterprise/src/app/* /usr/share/nginx/html && \  
cp -f /var/yunsoo/web-enterprise/nginx.server.conf
/etc/nginx/conf.d/default.conf && \  
rm -rf /var/yunsoo  
  
EXPOSE 80  

