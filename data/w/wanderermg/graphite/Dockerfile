FROM phusion/baseimage:0.9.16  
MAINTAINER Pavel Mironov <wanderermg@gmail.com>  
  
CMD ["/sbin/my_init"]  
  
RUN \  
curl -s http://nginx.org/keys/nginx_signing.key | apt-key add \- && \  
echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx-mainline.list && \  
apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get install python-dev -y && \  
apt-get install python-pip -y && \  
apt-get install python-cairo -y && \  
apt-get install nginx -y && \  
pip install django && \  
pip install tagging && \  
pip install django-tagging && \  
pip install uwsgi && \  
pip install whisper && \  
pip install carbon && \  
pip install graphite-web && \  
cd /opt/graphite/webapp/graphite && \  
cp local_settings.py.example local_settings.py && \  
sed -i -e "s/#SECRET_KEY = 'UNSAFE_DEFAULT'/SECRET_KEY = '`date | md5sum | cut
-d ' ' -f 1`'/" local_settings.py && \  
sed -i -e "s/#ALLOWED_HOSTS = \\[ '\\*' \\]/ALLOWED_HOSTS = \\[ '\\*' \\]/"
local_settings.py && \  
python manage.py syncdb --noinput && \  
chown www-data:www-data /opt/graphite/storage/graphite.db && \  
cd /opt/graphite/conf && \  
cp graphite.wsgi.example graphite.wsgi && \  
cp carbon.conf.example carbon.conf && \  
cp storage-schemas.conf.example storage-schemas.conf && \  
useradd -c "carbon user" -U -s /bin/false carbon && \  
chmod 775 /opt/graphite/storage && \  
chown www-data:carbon /opt/graphite/storage && \  
chown -R carbon /opt/graphite/storage/whisper && \  
chown www-data /opt/graphite/storage/log/webapp && \  
mkdir /etc/service/carbon-cache && \  
mkdir /etc/service/uwsgi && \  
mkdir /etc/service/nginx && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD carbon-cache.sh /etc/service/carbon-cache/run  
ADD uwgsi.graphite-web.ini /etc/uwsgi/graphite-web.ini  
ADD uwsgi.sh /etc/service/uwsgi/run  
ADD nginx.sh /etc/service/nginx/run  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443 2003 2003/udp 2004 2004/udp  
  
VOLUME [ "/opt/graphite/storage/whisper", "/opt/graphite/conf" ]  

