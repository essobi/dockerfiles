#  
# Nginx Dockerfile  
# version 1.1  
#  
FROM youpin/ubuntu  
MAINTAINER Leo <jiangwenhua@yoyohr.com>  
  
COPY home /home  
VOLUME /home/data  
  
#Update nginx.list  
COPY nginx.list /etc/apt/sources.list.d/nginx.list  
COPY nginx_signing.key /root/nginx_signing.key  
  
RUN apt-key add /root/nginx_signing.key \  
&& apt-get update \  
&& DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y nginx \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY nginx.conf /etc/nginx/  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  
  

