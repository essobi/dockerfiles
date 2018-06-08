FROM phusion/baseimage  
  
MAINTAINER magicalyak  
  
ENV DEBCONF_NONINTERACTIVE_SEEN="true" DEBIAN_FRONTEND="noninteractive"
DISABLESSH="true" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"  
ENV SHMEM="50%" TZ="Etc/UTC"  
VOLUME ["/config"]  
VOLUME ["/var/cache/zoneminder"]  
  
EXPOSE 80  
COPY install.sh /install.sh  
COPY firstrun.sh /etc/my_init.d/firstrun.sh  
COPY cambozola.jar /usr/share/zoneminder/www/cambozola.jar  
  
RUN bash /install.sh  
  
CMD ["/sbin/my_init"]  

