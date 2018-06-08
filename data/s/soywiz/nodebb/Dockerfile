FROM ubuntu:16.04  
MAINTAINER soywiz <soywiz@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#change it to your required node version  
ENV NODE_VERSION 6.9.5  
COPY files/install.sh /root/install.sh  
COPY files/nodeapp.sh /root/nodeapp.sh  
COPY files/nvm_install.sh /root/nvm_install.sh  
COPY files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV NVM_DIR /home/node/.nvm  
  
RUN chmod 777 /root/install.sh && /bin/bash -c "source /root/install.sh"  
  
VOLUME ["/var/lib/mongodb/", "/app"]  
  
EXPOSE 80 4567  
CMD ["/usr/bin/supervisord"]  

