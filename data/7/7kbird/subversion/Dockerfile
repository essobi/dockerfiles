FROM phusion/baseimage:0.9.18  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
RUN apt-get -y update -q  
  
# Fix "invoke-rc.d: policy-rc.d denied execution of start."  
RUN echo "#! /bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# Install apache and svn  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y apache2
subversion curl  
  
# Install modules for access control  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y libapache2-svn
libapache-dbi-perl \  
libapache2-mod-perl2 libauthen-simple-ldap-perl \  
libdbd-mysql-perl libdbd-pg-perl libdbd-sqlite3-perl  
  
# Install gettext for 'envsubst' to config with template  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y gettext  
  
RUN usermod -U www-data && chsh -s /bin/bash www-data  
  
RUN a2enmod dav dav_svn perl auth_digest  
  
RUN rm -fr /var/www /etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*  
#RUN mkdir -p /srv/svn /srv/apache  
#ADD apache2.conf /etc/apache2/apache2.conf  
ENV SVN_BUILD_DIR="/etc/svn-docker"  
# Add startup scripts for configuration  
RUN mkdir -p /etc/my_init.d  
ADD start.sh /etc/my_init.d/start.sh  
RUN chmod +x /etc/my_init.d/start.sh  
  
# Add apache as service  
ADD apache.service /etc/service/apache2/run  
RUN chmod +x /etc/service/apache2/run  
  
EXPOSE 80  
# Add build scripts  
COPY build/ ${SVN_BUILD_DIR}/  
ADD Redmine.pm /usr/lib/perl5/Apache/Redmine.pm  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

