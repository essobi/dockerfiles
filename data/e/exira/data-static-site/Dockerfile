FROM exira/base:3.4.2  
MAINTAINER exira.com <info@exira.com>  
  
RUN mkdir -p /var/www/public_html/  
WORKDIR /var/www/  
  
ONBUILD COPY ./public_html/ /var/www/public_html/  
ONBUILD COPY ./certs/ /etc/nginx/ssl/  
ONBUILD COPY ./nginx.conf /etc/nginx/sites/default.conf  
  
# ONBUILD RUN \  
# # Install build and runtime packages  
# build_pkgs="openssl" && \  
# apk update && \  
# apk upgrade && \  
# apk --update --no-cache add ${build_pkgs} && \  
# # Generate unique DH params  
# openssl dhparam -out /etc/nginx/ssl/dhparams.pem 4096 && \  
# # remove openssl dependencies  
# apk del ${build_pkgs} && \  
# # other clean up  
# cd / && \  
# rm -rf /var/cache/apk/* && \  
# rm -rf /tmp/*  
VOLUME /var/www/  
VOLUME /etc/nginx/sites/  
VOLUME /etc/nginx/ssl/  

