FROM codeserver/base  
MAINTAINER hello@neilellis.me  
  
RUN apt-get update && apt-get install -y nginx && apt-get autoremove -y &&
apt-get clean all  
ADD bin/nginx.sh /etc/service/nginx/run  
ADD etc/nginx.conf /etc/nginx/nginx.conf  
RUN chmod 755 /etc/service/nginx/run  
  
ENV SERVICE_ID ABC  
ENV SERVICE_ACCESS_TOKEN 123  
EXPOSE 80  

