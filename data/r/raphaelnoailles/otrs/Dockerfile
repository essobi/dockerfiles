FROM raphaelnoailles/baseimage:latest  
MAINTAINER Raphael Noailles <docker@noailles.de>  
  
# Set correct environment variables  
ENV HOME /root  
  
# don't ask for stupid things  
env DEBIAN_FRONTEND noninteractive  
  
# update the system  
RUN apt-get -y update && apt-get -y upgrade && dpkg-divert --local \--rename
--add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
RUN apt-get install -y locales locales-all  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Start conf  
# Install  
ADD scripts/install.sh /tmp/install.sh  
RUN chmod +x /tmp/install.sh  
RUN /bin/bash /tmp/install.sh  
# End conf  
# Set Apache environment variables (can be changed on docker run with -e)  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
ENV APACHE_DOCUMENTROOT /var/www  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80 443  
ADD /scripts/start.sh /usr/local/bin/start.sh  
RUN chmod 0755 /usr/local/bin/start.sh  
CMD ["bash", "/usr/local/bin/start.sh"]

