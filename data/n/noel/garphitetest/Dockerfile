#  
# Based on  
# https://github.com/cazcade/docker-grafana-graphite  
#  
FROM ubuntu:14.04  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ trusty universe' >>
/etc/apt/sources.list  
RUN apt-get -y update  
  
# Firewall cert, add as trusted  
ADD cert.crt /root/  
  
# Prerequisites  
RUN apt-get -y install python-django-tagging python-simplejson python-memcache
python-ldap python-cairo python-pysqlite2 python-support python-pip gunicorn
python-dev libpq-dev build-essential python-twisted  
  
RUN pip --cert /root/cert.crt install Django  
  
RUN apt-get -y install supervisor nginx-light git wget curl  
# Node  
RUN apt-get -y install software-properties-common  
  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash - # add
repository  
RUN apt-get install -y nodejs  
  
# Install StatsD  
RUN git config --global http.sslVerify false  
RUN git clone https://github.com/etsy/statsd.git /src/statsd  
  
# Install Whisper, Carbon and Graphite-Web  
RUN pip install pytz  
RUN pip install whisper  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
# Confiure StatsD  
ADD ./statsd/config.js /src/statsd/config.js  
  
# Configure Whisper, Carbon and Graphite-Web  
ADD ./graphite/initial_data.json
/var/lib/graphite/webapp/graphite/initial_data.json  
ADD ./graphite/local_settings.py
/var/lib/graphite/webapp/graphite/local_settings.py  
ADD ./graphite/carbon.conf /var/lib/graphite/conf/carbon.conf  
ADD ./graphite/storage-schemas.conf /var/lib/graphite/conf/storage-
schemas.conf  
ADD ./graphite/storage-aggregation.conf /var/lib/graphite/conf/storage-
aggregation.conf  
RUN mkdir -p /var/lib/graphite/storage/whisper  
  
RUN touch /var/lib/graphite/storage/graphite.db
/var/lib/graphite/storage/index  
RUN chown -R www-data /var/lib/graphite/storage  
RUN chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper  
RUN chmod 0664 /var/lib/graphite/storage/graphite.db  
RUN cd /var/lib/graphite/webapp/graphite && python manage.py syncdb --noinput  
  
# Configure nginx and supervisord  
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# StatsD  
EXPOSE 8125/udp  
EXPOSE 8126  
CMD ["/usr/bin/supervisord"]

