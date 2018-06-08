FROM alpine:3.4  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
ENV TERM vt100  
ENV WORDPRESS_VERSION 4.7.2  
ENV WORDPRESS_SHA1 7b687f1af589c337124e6247229af209ec1d52c3  
  
COPY . /build  
  
RUN /build/files/install_dependencies.sh  
RUN /build/files/prepare_php.sh  
  
# Apache config  
RUN /build/files/prepare_apache.sh  
  
# Setup wordpress  
COPY data /data  
RUN /build/files/prepare_wordpress.sh  
COPY files/htaccess /srv/wordpress/.htaccess  
COPY files/wp-config.php /srv/wp-config.php  
COPY files/msmtp /etc/msmtp.template  
  
# Scripts and entrypoint  
COPY scripts /scripts  
RUN mkdir /scripts/pre-init.d && \  
chmod -R 755 /scripts  
  
WORKDIR /srv  
EXPOSE 80  
VOLUME ["/srv/wordpress/wp-content/uploads"]  
ENTRYPOINT ["/scripts/run.sh"]  

