FROM debian:wheezy  
  
MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.7.6-1~wheezy  
  
RUN apt-get update && apt-get install -y nginx=${NGINX_VERSION}  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx", "/etc/nginx/conf.d"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

