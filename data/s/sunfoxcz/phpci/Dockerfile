FROM sunfoxcz/nginx-php7:0.1.0  
MAINTAINER Tomas Jacik <tomas@jacik.cz>  
  
ADD . /build  
  
RUN /build/prepare.sh && \  
/build/system_services.sh && \  
/build/cleanup.sh  
  
CMD ["/usr/local/bin/phpci"]  

