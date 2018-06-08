FROM debian:wheezy  
  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
  
ADD data/proxy.sh /etc/profile.d/proxy.sh  
RUN /etc/profile.d/proxy.sh  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get update && \  
apt-get install -y --no-install-recommends apache2 libapache2-mod-wsgi python
python-pip wget && \  
apt-get -y autoremove && \  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \mkdir -p /srv/http  
  
ADD data/run-apache /usr/local/bin/run-apache  
RUN chmod +x /usr/local/bin/run-apache  
  
ADD data/update-settings.py /usr/local/bin/update-settings.py  
RUN chmod +x /usr/local/bin/update-settings.py  
  
RUN pip install puppetboard  
  
ADD data/apache2.conf /etc/apache2/apache2.conf  
ADD data/apache-vhost-puppetboard /etc/apache2/sites-available/puppetboard  
ADD data/wsgi.py /srv/http/puppetboard/wsgi.py  
RUN chmod a+x /srv/http/puppetboard/wsgi.py  
RUN a2dissite default  
RUN a2ensite puppetboard  
  
# Enable the LDAP module  
RUN a2enmod authnz_ldap  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
CMD [ "/usr/local/bin/run-apache" ]  

