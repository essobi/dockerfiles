FROM stackbrew/debian:jessie  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nginx-light  
  
ADD default /etc/nginx/sites-available/default  
RUN (mkdir -p /var/www &&\  
echo "daemon off;" >> /etc/nginx/nginx.conf)  
  
EXPOSE 80  
CMD ["nginx","-c","/etc/nginx/nginx.conf"]  

