FROM ubuntu:14.04  
MAINTAINER Bart Reunes "@MetalArend"  
# Keep services disabled - http://serverfault.com/questions/567474/how-can-i-
install-packages-without-starting-their-associated-services  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Add keys  
#RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 40976EAF437D05B5  
# Add multiverse  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >>
/etc/apt/sources.list  
  
# Install packages  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -yq install \  
curl git \  
apache2 apache2-mpm-worker \  
libapache2-mod-fastcgi  
  
# Clean image  
RUN apt-get clean && \  
apt-get -f install && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /tmp/* /var/tmp/*  
  
# Add directories  
RUN mkdir -p /var/run/apache2 /var/lock/apache2 /var/lib/apache2/fastcgi  
  
# Set environment  
ENV APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_PID_FILE=/var/run/apache2/apache2.pid \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
APACHE_LOG_DIR=/var/log \  
APACHE_SERVER_ADMIN=admin@localhost \  
APACHE_SERVER_NAME=localhost \  
APACHE_HOST=* \  
APACHE_PORT=80 \  
APACHE_DOCUMENT_ROOT=/var/www/html \  
WORK_DIR=/var/www/html  
  
# Add & configure files  
#COPY ./conf/apache2.conf /etc/apache2/sites-available/001-docker.conf  
#RUN ln -s /etc/apache2/sites-available/001-docker.conf /etc/apache2/sites-
enabled/  
COPY ./conf/apache2.conf /etc/apache2/sites-enabled/000-default.conf  
#COPY ./conf/httpd.conf /usr/local/apache2/conf/httpd.conf  
#COPY ./conf/httpd.conf /etc/apache2/conf.d/php5-fpm.conf  
COPY ./conf/httpd.conf /etc/apache2/conf-available/php5-fpm.conf  
  
# Create directories  
RUN mkdir -pv "$APACHE_RUN_DIR" "$APACHE_LOCK_DIR" "$APACHE_LOG_DIR"  
  
# Enable services  
RUN a2enmod rewrite env actions fastcgi alias  
RUN a2enconf php5-fpm  
  
# Do not run apache2 here  
#RUN service apache2 restart # preferred instead of "/etc/init.d/apache2
restart"  
# Expose container  
EXPOSE 80 443  
WORKDIR "${WORK_DIR}"  
VOLUME ["$APACHE_LOG_DIR"]  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-help"]  

