FROM ubuntu:14.04  
RUN mkdir /opt/jumpserver  
COPY jumpserver /opt/jumpserver  
COPY files /opt/install  
RUN /opt/install/install.sh  
EXPOSE 80 22 389  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  

