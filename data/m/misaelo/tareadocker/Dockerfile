FROM debian:stretch  
  
MAINTAINER misael  
  
ENV DOCUMENTROOT /var/www/html  
ENV SERVERNAME supercontenedor  
ADD ./dnginx.sh /  
  
ENTRYPOINT ["/bin/bash","/dnginx.sh"]  
#RUN apt-get update \  
#&& apt-get install -y nginx  
EXPOSE 80  
#CMD ["nginx", "-g", "daemon off;"]  

