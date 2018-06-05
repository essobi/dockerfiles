FROM debian:jessie-backports  
MAINTAINER release@xcg-consulting.fr  
  
ADD etc /etc  
ADD usr /usr  
  
# In two lines for development  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy -t jessie-backports
python-django python-cryptography python-xstatic python-pip  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy python-authentic2
python-raven python-psycopg2 gunicorn  
RUN pip install authentic2-idp-oauth2  
# TODO logrotate install too much stuff, like cron (who asks for exim4)  
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy logrotate  
# do not include authentic2 as we suppose that both postgresql and nginx are
other dockers, not run inside this one  
RUN useradd --user-group --system authentic  
RUN mkdir -p /var/lib/authentic2/static && chown authentic:authentic -R
/var/lib/authentic2  
RUN mkdir /var/log/authentic2 && chown authentic:authentic /var/log/authentic2  
RUN sed -i 's|authentic2.sqlite3|/var/lib/authentic2/authentic2.sqlite3|'
/usr/lib/python2.7/dist-packages/authentic2/settings.py  
VOLUME ["/etc/authentic2/ssl", "/var/lib/authentic2/static"]  
ENTRYPOINT ["/usr/bin/authentic2"]  
CMD ["help"]  
EXPOSE 8000  

