##  
#  
# Docker file for nginx  
#  
##  
## Base Image  
FROM sunnybhanot/ubuntu  
  
## Install nginx  
RUN add-apt-repository -y ppa:nginx/stable \  
&& apt-get update -y \  
&& apt-get install nginx -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& chown -R www-data:www-data /var/lib/nginx  
## Define mountable directories  
VOLUME ["/etc/nginx", "/var/log/nginx", "/var/www/html"]  
  
## Define working directory  
WORKDIR /root  
  
## Define default command  
CMD ["nginx"]  
  
## Expose ports  
EXPOSE 80  
EXPOSE 443  

