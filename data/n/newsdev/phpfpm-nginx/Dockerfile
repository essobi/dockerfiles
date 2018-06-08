FROM php:7.1.3-fpm  
  
ENV NGINX_VERSION 1.10.1-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
RUN useradd --no-create-home nginx  
  
RUN apt-get update && \  
apt-get install -y ca-certificates nginx-extras && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  
  

