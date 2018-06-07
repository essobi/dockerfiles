# Debian: NGINX 1.9  
#  
# VERSION 0.0.1  
FROM debian:jessie  
  
ENV NGINX_VERSION 1.9.9-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62; \  
echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
RUN apt-get update && \  
apt-get install -y \  
openssl \  
ca-certificates \  
nginx=${NGINX_VERSION}  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
VOLUME ["/etc/nginx", "/var/log/nginx", "/var/cache/nginx"]  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT []  
  
CMD ["nginx"]  

