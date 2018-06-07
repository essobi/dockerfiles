FROM jakubzapletal/ubuntu:14.04.3  
# Install all prerequisites  
RUN \  
apt-get -y install software-properties-common && \  
add-apt-repository -y ppa:chris-lea/node.js && \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install python-django-tagging python-simplejson python-memcache
python-ldap python-cairo python-pysqlite2 python-support \  
python-pip gunicorn supervisor nginx-light nodejs git wget curl openjdk-7-jre
build-essential python-dev  
  
RUN \  
pip install Twisted==11.1.0 && \  
pip install Django==1.5  
  
# Install Elasticsearch  
RUN \  
cd /tmp && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.4.tar.gz
&& \  
tar xvzf elasticsearch-1.3.4.tar.gz && \  
rm -f elasticsearch-1.3.4.tar.gz && \  
mv /tmp/elasticsearch-1.3.4 /elasticsearch  
  
RUN mkdir /src  
  
# Install Whisper  
RUN \  
git clone https://github.com/graphite-project/whisper.git /src/whisper && \  
cd /src/whisper && \  
git checkout 0.9.x && \  
python setup.py install  
  
# Install Carbon  
RUN \  
git clone https://github.com/graphite-project/carbon.git /src/carbon && \  
cd /src/carbon && \  
git checkout 0.9.x && \  
python setup.py install  
  
# Install Graphite  
RUN \  
git clone https://github.com/graphite-project/graphite-web.git /src/graphite-
web && \  
cd /src/graphite-web && \  
git checkout 0.9.x && \  
python setup.py install  
  
# Install StatsD  
RUN \  
git clone https://github.com/etsy/statsd.git /src/statsd && \  
cd /src/statsd && \  
git checkout v0.7.2  
  
# Install Grafana  
RUN \  
mkdir /src/grafana && \  
wget http://grafanarel.s3.amazonaws.com/grafana-1.9.1.tar.gz -O
/src/grafana.tar.gz && \  
tar -xzf /src/grafana.tar.gz -C /src/grafana --strip-components=1 && \  
rm /src/grafana.tar.gz  
  
# Configure Elasticsearch  
ADD elasticsearch/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Configure Whisper, Carbon and Graphite-Web  
ADD graphite/initial_data.json /opt/graphite/webapp/graphite/initial_data.json  
ADD graphite/local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
ADD graphite/carbon.conf /opt/graphite/conf/carbon.conf  
ADD graphite/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf  
ADD graphite/storage-aggregation.conf /opt/graphite/conf/storage-
aggregation.conf  
RUN mkdir -p /opt/graphite/storage/whisper  
RUN touch /opt/graphite/storage/graphite.db /opt/graphite/storage/index  
RUN chown -R www-data /opt/graphite/storage  
RUN chmod 0775 /opt/graphite/storage /opt/graphite/storage/whisper  
RUN chmod 0664 /opt/graphite/storage/graphite.db  
RUN cd /opt/graphite/webapp/graphite && python manage.py syncdb --noinput  
  
# Confiure StatsD  
ADD statsd/config.js /src/statsd/config.js  
  
# Configure Grafana  
ADD grafana/config.js /src/grafana/config.js  
  
# Configure nginx and supervisord  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Expose ports  
# - 80: Grafana web interface  
# - 8125/udp: StatsD port  
# - 8126: StatsD administrative port  
EXPOSE 80 8125/udp 8126  
# Add the dashboards  
ADD grafana/dashboard-loader.js /src/dashboard-loader.js  
RUN mkdir -p /src/dashboards  
  
# Folder with data  
VOLUME /opt/graphite/storage/whisper  
  
# Folder with dashboards  
VOLUME /src/dashboards  
  
# Define default command  
CMD ["/usr/bin/supervisord"]  

