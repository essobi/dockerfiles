FROM ubuntu:16.04  
MAINTAINER Tomas Jacik <tomas@jacik.cz>  
  
ADD image /build  
  
# bower: cache  
ENV bower_storage__packages /cache/bower/packages  
ENV bower_storage__registry /cache/bower/registry  
ENV bower_storage__links /cache/bower/links  
  
# Configure Composer  
ENV COMPOSER_CACHE_DIR /cache/composer  
ENV COMPOSER_NO_INTERACTION 1  
# Composer: make global packages available for execution  
ENV PATH $PATH:~/.composer/vendor/bin  
  
RUN /build/prepare.sh && \  
/build/system_services.sh && \  
/build/packages.sh 7.2 && \  
/build/cleanup.sh  
  
CMD ["/sbin/my_init"]  

