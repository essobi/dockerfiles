FROM jgoerzen/proxied-app-apache:stretch  
  
# fckeditor is no longer in Debian but required for proper operation.  
  
RUN mv /usr/sbin/policy-rc.d.disabled /usr/sbin/policy-rc.d && \  
apt-get update && \  
apt-get -y -u dist-upgrade && \  
apt-get -y \--no-install-recommends install python-moinmoin wamerican \  
antiword catdoc poppler-utils python-xapian libapache2-mod-wsgi python-tz
python-flup python-recaptcha && \  
curl -s -o fckeditor_2.6.6-3_all.deb
'http://http.us.debian.org/debian/pool/main/f/fckeditor/fckeditor_2.6.6-3_all.deb'
&& \  
echo 6b8f516266d2a6be8b452ccae85416cf6c88f342b691b93853291b08a592f280
fckeditor_2.6.6-3_all.deb | sha256sum -c && \  
dpkg -i fckeditor_2.6.6-3_all.deb && \  
rm fckeditor_2.6.6-3_all.deb && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && /usr/local/bin/docker-wipelogs
&& \  
mv /usr/sbin/policy-rc.d /usr/sbin/policy-rc.d.disabled  
  
COPY conf-available/ /etc/apache2/conf-available/  
COPY sites-available/ /etc/apache2/sites-available/  
  
RUN a2enmod wsgi && \  
a2enconf docker-wsgi && \  
apache2ctl configtest  
  
CMD ["/usr/local/bin/boot-debian-base"]  

