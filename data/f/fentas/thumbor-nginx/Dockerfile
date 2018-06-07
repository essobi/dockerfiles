FROM apsl/thumbor  
MAINTAINER Jan Guth <jan.guth@gmail.com>  
  
MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.9.6-1~jessie  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD ./nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443 8000  
ENV NGINX_RESTRICT ""  
RUN \  
mkdir -p /etc/nginx/includes && \  
touch /etc/nginx/includes/nginx-restrict  
  
ADD docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

