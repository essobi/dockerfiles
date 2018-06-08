#  
# Based on  
# https://github.com/cazcade/docker-grafana-graphite  
#  
FROM ubuntu:14.04  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu/ trusty universe' >>
/etc/apt/sources.list  
RUN apt-get -y update  
  
# Prerequisites  
RUN apt-get -y install python-django-tagging python-simplejson python-memcache
python-ldap python-cairo python-pysqlite2 python-support python-pip gunicorn
python-dev libpq-dev build-essential  
# Why wont this work??  
#python-django python-twisted  
RUN pip install Twisted==11.1.0  
RUN pip install Django==1.5  
  
RUN apt-get -y install supervisor nginx-light git wget curl  
# Node  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:chris-lea/node.js  
RUN apt-get -y update  
RUN apt-get -y install nodejs  
# Elasticsearch  
RUN apt-get -y install openjdk-7-jre  
  
# Install Elasticsearch  
RUN mkdir /src && cd /src &&\  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.0.tar.gz
&&\  
tar xvzf elasticsearch-1.4.0.tar.gz && mv elasticsearch-1.4.0 elasticsearch
&&\  
rm -f elasticsearch-1.4.0.tar.gz  
RUN useradd elasticsearch --password elasticsearch  
RUN chown -R elasticsearch:elasticsearch /src/elasticsearch  
  
# Install StatsD  
RUN git clone https://github.com/etsy/statsd.git /src/statsd  
  
# Install Whisper, Carbon and Graphite-Web  
RUN pip install whisper  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon  
RUN pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
# Install Grafana  
RUN mkdir /src/grafana && cd /src/grafana &&\  
wget http://grafanarel.s3.amazonaws.com/grafana-1.9.0-rc1.tar.gz &&\  
tar xzvf grafana-1.9.0-rc1.tar.gz --strip-components=1 && rm
grafana-1.9.0-rc1.tar.gz  
  
# Configure Elasticsearch  
ADD ./elasticsearch/run /usr/local/bin/run_elasticsearch  
ADD ./elasticsearch/elasticsearch.yml
/src/elasticsearch/config/elasticsearch.yml  
  
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
  
# Configure Grafana  
ADD ./grafana/config.js /src/grafana/config.js  
#ADD ./grafana/scripted.json /src/grafana/app/dashboards/default.json  
# Configure nginx and supervisord  
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Grafana  
EXPOSE 80  
# Graphite ??  
EXPOSE 8000  
# Elasticserach  
EXPOSE 9200  
# StatsD  
EXPOSE 8125/udp  
EXPOSE 8126  
CMD ["/usr/bin/supervisord"]

