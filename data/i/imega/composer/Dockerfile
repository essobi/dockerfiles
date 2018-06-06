FROM imega/base-builder:1.2.0  
MAINTAINER Dmitry Gavriloff <info@imega.ru>  
  
ENV COMPOSER_CACHE_DIR=/cache  
  
ADD build/rootfs.tar.gz /  
  
ENTRYPOINT ["php", "/usr/bin/composer"]  

