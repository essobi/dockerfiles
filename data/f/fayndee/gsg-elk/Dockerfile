FROM debian:wheezy  
MAINTAINER Fang Yuan <fayndee@hotmail.com>  
  
# ---------------- #  
# Installation #  
# ---------------- #  
# Install prerequisites  
RUN echo 'deb http://http.debian.net/debian wheezy-backports main' >>
/etc/apt/sources.list.d/wheezy-backports.list  
RUN apt-get -y update  
# Node.js  
RUN apt-get -y --no-install-recommends install software-properties-common  
RUN apt-get -y --no-install-recommends -t wheezy-backports install nodejs  
# Python  
RUN apt-get -y --no-install-recommends install python python-colorama python-
django-tagging python-simplejson python-memcache python-ldap python-cairo
python-pysqlite2 python-support python-pip python-dev libpq-dev gunicorn
build-essential  
# Others  
RUN apt-get -y --no-install-recommends install supervisor nginx-light curl git
openjdk-7-jre adduser  
  
# Install Whisper, Carbon and Graphite-Web  
RUN pip install Twisted==11.1.0  
RUN pip install Django==1.5  
RUN pip install whisper  
RUN pip install carbon  
RUN pip install graphite-web  
  
# Install StatsD  
RUN git clone https://github.com/etsy/statsd.git /src/statsd \  
&& cd /src/statsd \  
&& git checkout v0.7.2  
  
# Install Grafana  
RUN mkdir /src/grafana  
RUN curl -o /src/grafana.tar.gz
http://grafanarel.s3.amazonaws.com/grafana-1.9.1.tar.gz \  
&& tar -xzf /src/grafana.tar.gz -C /src/grafana --strip-components=1 \  
&& rm /src/grafana.tar.gz  
  
# Install Elasticsearch  
RUN curl http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add
-  
RUN echo 'deb http://packages.elasticsearch.org/elasticsearch/1.4/debian
stable main' >> /etc/apt/sources.list.d/elasticsearch.list  
RUN apt-get update -y && apt-get -y --no-install-recommends install
elasticsearch  
  
# Install Logstash  
RUN echo 'deb http://packages.elasticsearch.org/logstash/1.4/debian stable
main' >> /etc/apt/sources.list.d/logstash.list  
RUN apt-get update -y && apt-get -y --no-install-recommends install logstash  
  
# Install Kibana  
RUN mkdir /src/kibana \  
&& curl -O https://download.elastic.co/kibana/kibana/kibana-3.1.2.tar.gz \  
&& tar xzvf kibana-3.1.2.tar.gz -C /src/kibana --strip-components=1 \  
&& rm -f kibana-3.1.2.tar.gz  
  
# ----------------- #  
# Configuration #  
# ----------------- #  
# Configure Whisper, Carbon and Graphite-Web  
ADD ./graphite/initial_data.json
/opt/graphite/webapp/graphite/initial_data.json  
ADD ./graphite/local_settings.py
/opt/graphite/webapp/graphite/local_settings.py  
ADD ./graphite/carbon.conf /opt/graphite/conf/carbon.conf  
ADD ./graphite/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf  
ADD ./graphite/storage-aggregation.conf /opt/graphite/conf/storage-
aggregation.conf  
RUN mkdir -p /opt/graphite/storage/whisper  
RUN touch /opt/graphite/storage/graphite.db /opt/graphite/storage/index  
RUN chmod 0775 /opt/graphite/storage /opt/graphite/storage/whisper  
RUN chmod 0664 /opt/graphite/storage/graphite.db  
RUN cd /opt/graphite/webapp/graphite && python manage.py syncdb --noinput  
  
# Confiure StatsD  
ADD ./statsd/config.js /src/statsd/config.js  
  
# Configure Grafana  
ADD ./grafana/config.js /src/grafana/config.js  
  
# Configure Elasticsearch  
RUN mkdir -p /usr/share/elasticsearch/config  
ADD ./elasticsearch/elasticsearch.yml
/usr/share/elasticsearch/config/elasticsearch.yml  
ADD ./elasticsearch/logging.yml /usr/share/elasticsearch/config/logging.yml  
  
# Configure Logstash  
ADD ./logstash/001-input-json-tcp.conf /etc/logstash/conf.d/001-input-json-
tcp.conf  
ADD ./logstash/002-input-json-udp.conf /etc/logstash/conf.d/002-input-json-
udp.conf  
ADD ./logstash/101-output-elasticsearch-local.conf
/etc/logstash/conf.d/101-output-elasticsearch-local.conf  
  
# Configure Kibana  
# Configure nginx and supervisord  
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf  
ADD ./supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# ---------------- #  
# Expose Ports #  
# ---------------- #  
# Carbon Cache (UDP/Line/Pickle)  
EXPOSE 2002/udp 2003 2004  
# Graphite Web  
EXPOSE 8000  
# StatsD (UDP/Management)  
EXPOSE 8125/udp 8126  
# Grafana  
EXPOSE 3000  
# Elasticsearch  
EXPOSE 9200  
# Logstash (TCP/UDP)  
EXPOSE 4560 4570/udp  
  
# Kibana  
EXPOSE 5601  
# -------- #  
# Run! #  
# -------- #  
CMD ["/usr/bin/supervisord"]  

