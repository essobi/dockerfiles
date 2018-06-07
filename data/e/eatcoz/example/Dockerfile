FROM ubuntu:14.04  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
supervisor \  
wget \  
curl  
  
# nodejs  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
RUN sudo apt-get install -y nodejs  
  
# nginx  
RUN wget http://nginx.org/keys/nginx_signing.key  
RUN apt-key add nginx_signing.key  
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
RUN echo "deb-src http://nginx.org/packages/ubuntu/ trusty nginx" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y nginx  
  
# Workaround for bug in Virtualbox that corrupts "bundle.js"  
# http://quyennt.com/web-development/chrome-js-syntaxerror-unexpected-token-
illegal-caused-by-vagrant-synced-folder/  
RUN sed -i "s/sendfile on/sendfile off/g" /etc/nginx/nginx.conf  
  
# To be provided via volume: /nginx/default.conf  
RUN mkdir /nginx  
RUN mv /etc/nginx/conf.d/default.conf /nginx  
RUN ln -s /nginx/default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80  
WORKDIR /src  
CMD ["/usr/bin/supervisord", "-c", "/supervisor/supervisord.conf"]

