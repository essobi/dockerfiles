FROM ubuntu:latest  
  
# Package installs  
RUN apt-get -y update && apt-get install -y python2.7 python-flask python-
dateutil python-tz python-pip apache2 libapache2-mod-wsgi  
RUN /usr/bin/pip install Flask-SQLAlchemy  
  
# Apache setup  
RUN /bin/ln -s /etc/webapp/webapp.conf /etc/apache2/sites-
available/webapp.conf  
RUN /bin/rm -f /etc/apache2/sites-enabled/000-default.conf  
RUN /usr/sbin/a2enmod wsgi.load  
  
# Flask setup  
ADD conf/webapp.conf /etc/webapp/webapp.conf  
ADD webapp/ /var/www/webapp/  
RUN chown -R www-data.www-data /var/www/webapp  
  
# Startup  
RUN /usr/sbin/a2ensite webapp.conf  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

