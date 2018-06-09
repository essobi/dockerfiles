FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install -y apache2-utils nginx  
  
# NGINX PROXY  
EXPOSE 8080  
EXPOSE 8081  
EXPOSE 80  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD run.sh run.sh  
  
CMD bash run.sh  

