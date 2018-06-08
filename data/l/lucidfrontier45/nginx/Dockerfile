FROM ubuntu:xenial  
LABEL maintainer="Shiqiao Du <lucidfrontier.45@gmail.com>"  
  
ENV NGINX_VERSION 1.11.9-1~xenial  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62
\  
&& echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
nginx-module-xslt \  
nginx-module-geoip \  
nginx-module-image-filter \  
nginx-module-perl \  
nginx-module-njs \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80 443  
  
CMD ["nginx", "-g", "daemon off;"]

