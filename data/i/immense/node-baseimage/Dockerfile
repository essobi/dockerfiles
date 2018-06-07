FROM node:0.12  
MAINTAINER Christian Bankester <cbankester@immense.net>  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
ENV NGINX_VERSION 1.9.0-1~jessie  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN npm install -g bower  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  

