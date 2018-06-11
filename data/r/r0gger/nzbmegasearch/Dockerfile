FROM linuxserver/baseimage.python  
MAINTAINER ROGGER  
  
# add some files  
ADD services/ /etc/service/  
ADD init/ /etc/my_init.d/  
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh  
  
# ports and volumes  
EXPOSE 5000  
VOLUME /config  

