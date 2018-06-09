FROM frekele/nginx:1  
MAINTAINER frekele <leandro.freitas@softdevelop.com.br>  
  
# Add the files  
ADD rootfs /  
  
# Print default.conf to see all config.  
RUN cat /etc/nginx/conf.d/default.conf  
  
#Open port 81 for health_check.  
EXPOSE 80 81  

