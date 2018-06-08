# nginx-full  
# https://github.com/nmarus/docker-images  
# Nicholas Marus <nmarus@gmail.com>  
FROM debian:jessie  
MAINTAINER Nicholas Marus <nmarus@gmail.com>  
  
# Setup Container  
VOLUME ["/var/cache/nginx"]  
EXPOSE 80 443  
# Setup APT  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Update, Install Prerequisites, Clean Up APT  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y update && \  
apt-get -y install git curl nginx-full && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
CMD ["nginx", "-g", "daemon off;"]  

