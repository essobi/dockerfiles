FROM nginx  
  
MAINTAINER stevehopkinson <stevehopkinson@stevehopkinson.co.uk>  
  
# Update and requirements for extensions  
RUN apt-get update \  
&& apt-get install -y \  
vim  
  
COPY config/codeigniter.conf /etc/nginx/conf.d/codeigniter.conf  
COPY config/nginx.conf /etc/nginx/nginx.conf  

