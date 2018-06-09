FROM ubuntu:16.04  
LABEL maintainer="gyorgy.novak@loxxly.com"  
  
COPY svn.conf /etc/apache2/sites-available/  
  
RUN apt-get update \  
&& apt-get install -y apache2 subversion libapache2-svn \  
&& rm -r /var/lib/apt/lists/* \  
&& ln -s /etc/apache2/sites-available/svn.conf /etc/apache2/sites-
enabled/svn.conf \  
&& ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-
enabled/headers.load  
  
# Configure Apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
env APACHE_PID_FILE /var/run/apache2.pid  
env APACHE_RUN_DIR /var/run/apache2  
env APACHE_LOCK_DIR /var/lock/apache2  
env APACHE_LOG_DIR /var/log/apache2  
  
# Expose ourselves  
EXPOSE 80  
# Run!  
ENTRYPOINT [ "/usr/sbin/apache2", "-DFOREGROUND" ]  

