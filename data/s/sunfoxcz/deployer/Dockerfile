FROM sunfoxcz/nginx-php7:latest  
MAINTAINER Tomas Jacik <tomas@jacik.cz>  
  
ADD . /build  
  
RUN /build/prepare.sh && \  
/build/system_services.sh && \  
/build/cleanup.sh  
  
CMD ["/usr/local/bin/deployer"]  

