FROM debian:wheezy  
  
# MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"  
MAINTAINER Jesus Franco "jefrancomix@gmail.com"  
# Importing key from public keys directory  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
# Add nginx repo to sources.list  
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.7.10-1~wheezy  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&
DEBIAN_FRONTEND=noninteractive apt-get install -y nginx=${NGINX_VERSION} && rm
-rf /var/lib/apt/lists/*  
  
# forward request logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx","/etc/nginx"]  
  
EXPOSE 80 443  
ENTRYPOINT ["nginx"]  
  
CMD ["-g", "daemon off;"]  
  

