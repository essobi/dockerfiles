# Based on https://github.com/nginxinc/docker-nginx/blob/master/Dockerfile  
FROM debian:wheezy  
  
MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.7.11-1~wheezy  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Install our own nginx conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Remove the default nginx file  
RUN rm -f /etc/nginx/sites-enabled/default  
  
# Define mountable directories.  
VOLUME ["/var/log/nginx"]  
  
# Define working directory.  
WORKDIR /etc/nginx  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]

