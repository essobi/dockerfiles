FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# these deps are from two tutorials:  
# - http://graphite.readthedocs.org/en/latest/install.html  
# - https://gist.github.com/jgeurts/3112065  
RUN echo "===> Install the basics..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -yq --force-yes \  
apache2 \  
fontconfig \  
libcairo2 \  
libcairo2-dev \  
memcached \  
python-cairo-dev \  
python-dev \  
python-django \  
python-django-tagging \  
python-ldap \  
python-memcache \  
python-pysqlite2 \  
python-pip \  
python-setuptools \  
rabbitmq-server \  
ssh \  
sqlite3 && \  
pip install \  
carbon \  
django-tagging \  
graphite-web \  
python-memcached \  
pytz \  
txAMQP \  
twisted \  
whisper && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* tmp/* /var/tmp/*  
  
RUN echo "===> Setup carbon..." && \  
cd /opt/graphite/conf && \  
cp carbon.conf.example carbon.conf && \  
cp storage-schemas.conf.example storage-schemas.conf && \  
echo "[stats]" >> storage-schemas.conf && \  
echo "Pattern = ^stats.*" >> storage-schemas.conf && \  
echo "Retentions = 10s:6h,1min:7d,10min:5y" >> storage-schemas.conf  
  
RUN echo "===> Setup graphite..." && \  
cd /opt/graphite/examples && \  
cp example-graphite-vhost.conf /etc/apache2/sites-available/default && \  
cp /opt/graphite/conf/graphite.wsgi.example /opt/graphite/conf/graphite.wsgi
&& \  
mkdir /etc/httpd && \  
mkdir /etc/httpd/wsgi && \  
sed -i "s/WSGISocketPrefix run\/wsgi/WSGISocketPrefix \/etc\/httpd\/wsgi/g"
/etc/apache2/sites-available/default && \  
/etc/init.d/apache2 restart && \  
/etc/init.d/apache2 reload  
  
RUN echo "===> Setup inital database..." && \  
cd /opt/graphite/webapp/graphite/ && \  
python manage.py syncdb --noinput && \  
chown -R www-data:www-data /opt/graphite/storage/ && \  
/etc/init.d/apache2 restart && \  
cd /opt/graphite/webapp/graphite && \  
cp local_settings.py.example local_settings.py  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

