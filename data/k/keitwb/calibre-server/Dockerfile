FROM keitwb/calibre-base:2.59  
MAINTAINER Ben Keith <keitwb@gmail.com>  
ENTRYPOINT ["/entrypoint"]  
  
RUN touch /var/log/calibre.log &&\  
chown calibre:calibre /var/log/calibre.log  
  
USER calibre  
EXPOSE 8080  
COPY entrypoint /entrypoint  

