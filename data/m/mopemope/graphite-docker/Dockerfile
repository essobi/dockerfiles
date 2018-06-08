FROM ubuntu:14.04  
  
MAINTAINER mopemope yutaka.matsubara@gmail.com  
  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local --rename --add /sbin/initctl && rm -f /sbin/initctl &&
ln -s /bin/true /sbin/initctl  
  
RUN apt-get -yq update && apt-get install -y apt-cacher-ng language-pack-en
language-pack-ja  
#RUN echo 'Acquire::http::Proxy "http://172.17.42.1:3142";' >
/etc/apt/apt.conf.d/02proxy.conf  
  
RUN chmod go+w,u+s /tmp  
  
# Install required packages  
RUN apt-get -qy upgrade && apt-get -y install build-essential git python-ldap
python-cairo python-django-tagging python-simplejson python-memcache python-
pysqlite2 python-support python-pip gunicorn supervisor nginx python-all-dev
wget curl openjdk-7-jdk nodejs npm --no-install-recommends  
  
#RUN /bin/echo -e "LANG=\"ja_JP.UTF-8\"" > /etc/default/local \  
# && echo "Asia/Tokyo" > /etc/timezone \  
# && dpkg-reconfigure -f noninteractive tzdata  
# ES  
RUN cd ~ && wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.0.1.deb
\  
&& cd ~ && dpkg -i elasticsearch-1.0.1.deb && rm elasticsearch-1.0.1.deb \  
&& apt-get clean  
ADD ./elasticsearch/run_elasticsearch /usr/local/bin/run_elasticsearch  
  
# graphite  
  
RUN pip install 'Twisted<12.0' 'django<1.6' \  
&& pip install whisper \  
&& pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon \  
&& pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
# grafana  
RUN mkdir -p /src/grafana && cd /src/grafana &&\  
wget http://grafanarel.s3.amazonaws.com/grafana-1.5.4.tar.gz &&\  
tar -xzvf grafana-1.5.4.tar.gz && rm grafana-1.5.4.tar.gz  
ADD ./grafana/config.js /src/grafana/grafana-1.5.4/  
  
# statsd  
RUN git clone https://github.com/etsy/statsd.git /src/statsd  
ADD ./statsd/config.js /src/statsd/config.js  
  
# Add system service config  
ADD ./nginx/nginx.conf /etc/nginx/nginx.conf  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add graphite config  
ADD ./graphite/initial_data.json
/var/lib/graphite/webapp/graphite/initial_data.json  
ADD ./graphite/local_settings.py
/var/lib/graphite/webapp/graphite/local_settings.py  
ADD ./graphite/carbon.conf /var/lib/graphite/conf/carbon.conf  
ADD ./graphite/storage-schemas.conf /var/lib/graphite/conf/storage-
schemas.conf  
  
RUN mkdir -p /var/lib/graphite/storage/whisper \  
&& touch /var/lib/graphite/storage/graphite.db /var/lib/graphite/storage/index
\  
&& chown -R www-data /var/lib/graphite/storage \  
&& chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper \  
&& chmod 0664 /var/lib/graphite/storage/graphite.db \  
&& cd /var/lib/graphite/webapp/graphite && python manage.py syncdb \--noinput
\  
&& chmod 0755 /usr/local/bin/run_elasticsearch  
  
# Nginx port 80 81  
# Carbon line receiver port 2003  
# Carbon pickle receiver port 2004  
# Carbon cache query port 7002  
# Statsd UDP port 8125:8125/udp  
# Statsd Management port 8126  
EXPOSE 80 81 2003 2004 7002 8125/udp 8126  
  
VOLUME ["/var/graphite/storage", "/var/lib/elasticsearch"]  
  
CMD ["/usr/bin/supervisord"]  

