FROM nginx:1.11.9  
MAINTAINER Suparit Krityakien <suparit@wongnai.com>  
  
# Install useful utilities  
RUN apt-get update -y \  
&& apt-get install -y \  
logrotate \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY nginx/ /etc/nginx/  
COPY nginxrt/ /etc/nginxrt/  
COPY nginx.logrotate.conf /etc/logrotate.d/  

