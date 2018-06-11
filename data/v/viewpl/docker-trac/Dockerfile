# Reference:  
# http://trac.edgewall.org/wiki/Ubuntu-10.04.03-Git  
# http://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:0.9.15  
MAINTAINER Rob Lao "viewpl@gmail.com"  
ENV HOME /root  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Add public key for ssh service  
ADD key.pub /root/.ssh/authorized_keys  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_USER_UID 0  
RUN apt-get update  
  
# Install Apache2...  
RUN apt-get install -y apache2 apache2-utils libapache2-mod-python python-
setuptools python-genshi  
RUN a2enmod python  
RUN a2enmod rewrite  
  
# Install MySQL...  
RUN echo 'mysql-server mysql-server/root_password password docker-trac1A~' |
debconf-set-selections  
RUN echo 'mysql-server mysql-server/root_password_again password docker-
trac1A~' | debconf-set-selections  
RUN apt-get install -y mysql-server  
RUN apt-get install -y python-mysqldb  
  
# Install git and Trac  
RUN apt-get install -y git-core  
RUN apt-get install -y trac trac-git  
  
# Add deploy key for git repo  
ADD deploy_key /root/.ssh/deploy_key  
  
# Trac  
RUN mkdir /usr/local/trac  
RUN mkdir /usr/local/trac/docker-trac-demo  
  
# Configure MySQL  
ADD my.cnf /root/.my.cnf  
  
# Configure Trac  
ADD trac.ini /usr/local/trac/trac.ini  
RUN cd /usr/local/trac && htpasswd -bc .htpasswd admin docker-trac1A~  
  
# Configure Apache  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
  
# Install entrypoint  
ADD entrypoint.sh /etc/my_init.d/entrypoint.sh  
RUN chmod +x /etc/my_init.d/entrypoint.sh  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 80  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

