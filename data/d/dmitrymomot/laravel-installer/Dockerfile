FROM dmitrymomot/composer  
  
MAINTAINER "Dmitry Momot" <mail@dmomot.com>  
  
RUN mkdir /laravel-installer  
WORKDIR /laravel-installer  
  
RUN composer require "laravel/installer" && \  
ln -s /laravel-installer/vendor/laravel/installer/laravel
/usr/local/bin/laravel && \  
chmod +x /usr/local/bin/laravel  
  
RUN mkdir -p /data  
VOLUME ["/data"]  
WORKDIR /data  
  
ENTRYPOINT ["laravel"]  
CMD ["--help --ansi"]  

