FROM ubuntu:12.04  
MAINTAINER Kamil Trzciński <ayufan@ayufan.eu>  
  
ADD ./stack/ /build  
RUN /build/prepare  
  
# fix php buildpack, source: https://github.com/deis/heroku-buildpack-
php/commit/d305d7eb5f45959b54e1b9729b0cd36685c8126d  
RUN sed -i 's|^;listen.mode = 0666|listen.mode = 0666|g'
/build/buildpacks/*/conf/php/php-fpm.conf  
  
#fix php buildpack, source: https://github.com/drmikecrowe/dokku-buildpack-
php/commit/00cf93c2f3a60e11f9d4e81a7c110977dbddee41  
RUN mkdir /root/bin  
  
ENV PORT 5000  
EXPOSE 5000  

