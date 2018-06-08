# download large base image  
FROM ubuntu:14.04  
# env  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/run/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV BUILD_DIR /build  
ENV SRC_DIR $BUILD_DIR/bash-4.3  
ENV APT apt-get  
ENV APT_UPDATE $APT update  
ENV APT_INSTALL $APT install --no-install-recommends -y  
ENV MKDIR mkdir -p  
ENV TARFILE bash-4.3.tar.gz  
  
# install apache  
RUN $APT_UPDATE  
RUN $APT_INSTALL apache2  
RUN $MKDIR /var/run/apache2  
  
# add cgi bash script  
ADD cgi-bin/shockme.cgi /usr/lib/cgi-bin/  
RUN chmod +x /usr/lib/cgi-bin/shockme.cgi  
RUN a2enmod cgid  
  
# install vulnerable bash  
RUN $APT_INSTALL build-essential  
RUN $MKDIR $BUILD_DIR  
ADD $TARFILE $BUILD_DIR  
RUN cd $SRC_DIR && ./configure  
RUN cd $SRC_DIR && make  
RUN cd $SRC_DIR && make install  
  
# documents intended exposed port (no other function)  
EXPOSE 80  
#  
ENTRYPOINT ["/usr/sbin/apache2"]  
  
#  
CMD ["-D", "FOREGROUND"]  
  

