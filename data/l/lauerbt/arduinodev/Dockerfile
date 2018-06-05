FROM ubuntu:16.04  
MAINTAINER thomas@lauerbach.de  
  
ENV CONTAINER_VERSION 1.0  
# ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib  
ADD customisation /opt/customisation/  
  
RUN ["/opt/customisation/init.sh"]  
  
VOLUME /volumes/workspaces  
  
CMD ["/usr/bin/xterm"]  

