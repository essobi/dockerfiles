FROM ubuntu:trusty  
ENV DEBIAN_FRONTEND noninteractive  
MAINTAINER Stefan Liedle  
  
# nginx  
RUN apt-get update -q  
RUN apt-get install -yf build-essential python-software-properties software-
properties-common  
RUN add-apt-repository ppa:nginx/stable  
RUN apt-get update -q  
RUN apt-get -y install -y curl  
  
ENV NGINX_VERSION 1.9.6  
# build nginx from source with http auth module enabled  
RUN apt-get -y install libpcre3-dev zlib1g-dev libssl-dev  
RUN curl -O http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz  
RUN tar -xzf nginx-${NGINX_VERSION}.tar.gz  
WORKDIR nginx-${NGINX_VERSION}  
RUN ./configure --with-http_ssl_module --with-http_auth_request_module && make
&& make install  
  
# install pystache  
RUN apt-get -y install python-pip  
RUN pip install pystache  
  
# nginx configuration  
ADD nginx/nginx.conf /usr/local/nginx/conf/nginx.conf  
ADD nginx/nginx.default /usr/local/nginx/conf/sites-enabled/default.template  
ADD start.sh /start.sh  
  
EXPOSE 80  
CMD /start.sh  

