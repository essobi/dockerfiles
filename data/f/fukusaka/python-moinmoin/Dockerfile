FROM ubuntu:16.04  
MAINTAINER fukusaka  
  
RUN apt-get update -qq  
RUN apt-get -qqy install apache2 libapache2-mod-wsgi  
RUN apt-get -qqy install lsb-invalid-mta  
RUN apt-get -qqy install python-moinmoin  
RUN apt-get -qqy install language-pack-ja  
  
RUN adduser moin --system --group --uid 1000  
RUN mkdir /srv/moin  
RUN chown -R moin:moin /usr/share/moin/underlay  
  
RUN mkdir /srv/moin/mywiki  
RUN cp -r /usr/share/moin/data /usr/share/moin/underlay /srv/moin/mywiki  
  
RUN mkdir /srv/moin/mywiki/html  
COPY conf/apache2-moin.conf /etc/apache2/sites-available/moin.conf  
RUN a2dissite 000-default  
RUN a2ensite moin  
  
COPY conf/moin-farmconfig.py /etc/moin/farmconfig.py  
COPY conf/moin-mywiki.py /etc/moin/mywiki.py  
  
#RUN moin --config-dir=/etc/moin/ --wiki-url=http://localhost/ account create
--name 'admin' --password='moinmoin' --email='admin@example.org'  
RUN chown -R moin:moin /srv/moin/mywiki  
RUN chmod -R ug+rwX /srv/moin/mywiki  
RUN chmod -R o-rwx /srv/moin/mywiki  
RUN addgroup www-data moin  
  
VOLUME "/srv/moin/mywiki/data/pages"  
  
EXPOSE 80  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV LANG ja_JP.UTF-8  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

