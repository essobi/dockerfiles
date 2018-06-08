FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.utf8  
  
ENV LC_All en_US.utf8  
  
# install packages  
RUN apt-get install -y software-properties-common ;\  
apt-get update ;\  
apt-get install -y nano apache2 apache2-utils curl libapache2-mod-wsgi wget
gcc python-dev  
  
# Enable apache modules  
RUN a2enmod rewrite ;\  
a2enmod wsgi ;\  
a2enmod ldap ;\  
a2enmod authnz_ldap  
  
ADD etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/000-default.conf  
  
# install mercurial from source  
RUN wget https://www.mercurial-scm.org/release/mercurial-3.5.2.tar.gz -O
/tmp/mercurial-3.5.2.tar.gz ;\  
tar -xzvf /tmp/mercurial-3.5.2.tar.gz -C /tmp ;\  
cd /tmp/mercurial-3.5.2 ;\  
python2 setup.py install --force --home=/usr  
  
# Add global hgrc file  
# ADD etc/mercurial/hgrc /etc/mercurial/hgrc  
# Set up hgweb  
ADD ./var/www/scripts/hgwebdir.wsgi /var/www/scripts/hgwebdir.wsgi  
ADD ./var/www/hgweb.config /var/www/hgweb.config  
  
ENV DEBIAN_FRONTEND dialog  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
# make repositories dir  
RUN mkdir /var/repositories  
  
VOLUME ["/var/www", "/var/repositories"]  
  
ENTRYPOINT ["/usr/sbin/apache2"]  
CMD ["-D", "FOREGROUND"]  

