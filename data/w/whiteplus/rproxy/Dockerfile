FROM debian:jessie  
  
MAINTAINER WHITEPLUS System "sysadmin@wh-plus.com"  
  
ENV NGINX_VERSION 1.9.5-1~jessie  
  
RUN /bin/cp -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \  
&& apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update 1> /dev/null \  
&& apt-get upgrade -y -q --no-install-recommends \  
&& apt-get install -y --no-install-recommends ca-certificates
nginx=${NGINX_VERSION} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

