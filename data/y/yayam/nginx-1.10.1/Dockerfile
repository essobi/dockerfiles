FROM yayam/debian-jessie  
# COPY FROM https://github.com/nginxinc/docker-
nginx/blob/11fc019b2be3ad51ba5d097b1857a099c4056213/stable/jessie/Dockerfile  
ENV NGINX_VERSION 1.10.2-1~jessie  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get autoremove \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
# nginx-module-xslt \  
# nginx-module-geoip \  
# nginx-module-image-filter \  
# nginx-module-perl \  
# nginx-module-njs \  
# gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
#  
# Add user johnsnow user to www-data  
#RUN useradd -g www-data johnsnow  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

