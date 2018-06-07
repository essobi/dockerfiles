FROM ubuntu:14.04  
MAINTAINER Danny,Ho <danny.ho@hpe.com>  
RUN apt-get update  
RUN apt-get -y install \  
nginx  
RUN sed -i '42 i\location /GOOGLE { \  
proxy_pass http://www.google.com; \  
}' /etc/nginx/sites-available/default  
ENTRYPOINT service nginx restart && bash  

