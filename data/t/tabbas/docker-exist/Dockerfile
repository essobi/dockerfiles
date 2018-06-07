FROM java:latest  
MAINTAINER Andreas Jung <info@zopyx.com>  
  
RUN apt-get update  
RUN apt-get install -y curl expect cadaver  
  
WORKDIR /root  
RUN curl -LO http://downloads.sourceforge.net/exist/Stable/2.2/eXist-db-
setup-2.2.jar  
ADD exist-setup.cmd /root/exist-setup.cmd  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
#RUN expect -f exist-setup.cmd  
#RUN rm eXist-db-setup-2.2.jar exist-setup.cmd  
EXPOSE 8080 8443  
ENV EXIST_HOME /opt/exist  
ENV EXIST_PASSWORD admin  
WORKDIR /opt/exist  
VOLUME /opt/exist-data  
  
CMD ["/entrypoint.sh"]

