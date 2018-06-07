FROM existenz/base  
  
MAINTAINER docker@stefan-van-essen.nl  
  
RUN apk -U add --no-cache \  
git \  
php7 \  
php7-json \  
php7-mbstring \  
php7-phar \  
php7-openssl \  
php7-zip \  
php7-zlib \  
subversion  
  
COPY install-composer.sh /tmp  
  
RUN cd /app \  
&& sh /tmp/install-composer.sh \  
&& rm -rf /tmp/*  
  
# Remove this user and group because they use ID 1000 and thus collide with
runas  
RUN deluser svn && delgroup svnusers  
  
WORKDIR /cwd  
  
ENTRYPOINT ["runas", "/app/composer.phar", "--ansi"]  

