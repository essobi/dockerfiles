FROM centos:centos7  
  
MAINTAINER Dmitry Orlov <me@mosquito.su>  
  
RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum localinstall -y
http://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-
release-1.0-13.ius.centos7.noarch.rpm  
RUN yum localinstall -y
http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-1.noarch.rpm  
RUN yum install -y http://nginx.org/packages/centos/7/noarch/RPMS/nginx-
release-centos-7-0.el7.ngx.noarch.rpm  
  
RUN yum upgrade -y  
  
RUN yum groupinstall -y 'Development Tools'  
RUN yum install -y zlib-devel python-devel libxslt-devel wget \  
libxml2-devel libyaml-devel libpng-devel libjpeg-devel python-pip \  
cython python-psycopg2 python-lxml nginx nodejs pycairo memcached supervisor \  
expect net-tools rrdtool-devel  
  
RUN mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled
/etc/nginx/conf.d  
  
RUN pip install "django<1.6" "python-memcached" \  
"django-tagging>=0.3.1" "twisted<12" \  
"txAMQP==0.6.2" "flup" "rrdtool"  
  
RUN pip install "https://github.com/graphite-project/ceres/tarball/master" \  
carbon whisper graphite-web \  
\--install-option="--install-scripts=/usr/bin" \  
\--install-option="--install-lib=/usr/lib/python2.7/site-packages" \  
\--install-option="--install-data=/var/lib/graphite"  
  
RUN groupadd -g 1000 graphite && useradd -c "Graphite" -u 1000 -g 1000
graphite  
  
# install graphite  
RUN pip install https://github.com/graphite-project/graphite-
web/archive/0.9.12.zip  
  
# install whisper  
RUN pip install https://github.com/graphite-project/whisper/archive/0.9.12.zip  
  
# install carbon  
RUN pip install https://github.com/graphite-project/carbon/archive/0.9.12.zip  
  
# install statsd  
RUN mkdir -p /opt/statsd && cd /opt/statsd && \  
wget https://github.com/etsy/statsd/archive/v0.7.2.tar.gz -O - | tar xvz  
  
RUN pip install j2cli  
  
# RUN PYTHONPATH=/opt/graphite/webapp django-admin.py collectstatic --noinput
--settings=graphite.settings  
ENV ADMIN_USER=admin ADMIN_PASSWORD=admin ADMIN_EMAIL=admin@example.net  
  
# logging support  
RUN mkdir -p /var/log/carbon /var/log/graphite /var/log/nginx  
  
ENV DEBUG=0  
ENV SECRET_KEY=MY_SUPER_SECRET  
ENV LOG_RENDERING_PERFORMANCE=0 LOG_CACHE_PERFORMANCE=0 LOG_METRIC_ACCESS=0  
COPY configs/graphite/*.conf /opt/graphite/conf/  
  
# config nginx  
COPY configs/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY configs/nginx/graphite.conf /etc/nginx/sites-enabled/graphite.conf  
  
COPY configs/statsd/config.js /opt/statsd/config.js  
  
COPY configs/supervisor/supervisord.conf /etc/supervisord.conf  
COPY configs/supervisor/*.ini /etc/supervisord.d/  
  
# add templates  
RUN mkdir -p /etc/templates  
COPY configs/scripts/django_admin_init.exp
/etc/templates/django_admin_init.exp.j2  
  
# start.sh  
COPY configs/start.sh /usr/local/bin/start.sh  
RUN chmod a+x /usr/local/bin/start.sh  
  
COPY configs/local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
  
# defaults  
EXPOSE 80:80 2003:2003 2003:2003/udp 8125:8125/udp  
VOLUME [ "/opt/graphite/storage", "/var/log/supervisor" ]  
  
CMD ["/usr/local/bin/start.sh"]  

