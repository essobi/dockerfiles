FROM alpine:3.7  
LABEL maintainer="Mark Woolley <mw@marknet15.com>"  
LABEL version="0.6.5"  
LABEL description="Apache Docker Container"  
  
# Install required packages  
RUN apk add --update --no-cache \  
bash \  
bash-doc \  
bash-completion \  
apache2 \  
apache2-ssl \  
apache2-utils \  
apache2-proxy \  
apache2-proxy-html \  
apache2-ldap \  
libxml2-dev \  
php7 \  
php7-apache2 \  
php7-mysqli \  
php7-zlib \  
php7-curl \  
php7-json \  
php7-session \  
php7-pear \  
php7-opcache  
  
# Stream the Apache logs & create required dirs  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log && \  
mkdir /run/apache2/ && \  
mkdir web && \  
mkdir /web/www && \  
mkdir /web/certs && \  
mkdir /web/vhosts  
  
# Add volume for persistant app config  
VOLUME [ "/web/www" ]  
VOLUME [ "/web/vhosts" ]  
VOLUME [ "/web/certs" ]  
  
# Add httpd conf file  
COPY httpd.conf /etc/apache2/httpd.conf  
  
# Expose port to outside world  
EXPOSE 80 443  
# Entrypoint for container  
CMD ["-D", "FOREGROUND"]  
ENTRYPOINT ["httpd"]

