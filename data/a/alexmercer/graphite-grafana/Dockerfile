# DOCKER-VERSION 0.4.0  
  
from ubuntu:trusty  
run apt-get -y update  
  
# Install required packages  
run apt-get -y install python-ldap python-cairo python-django python-twisted
python-django-tagging python-simplejson python-memcache python-pysqlite2
python-support python-pip gunicorn supervisor nginx-light wget  
run pip install whisper  
run pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon  
run pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
# Grafana  
run wget https://grafanarel.s3.amazonaws.com/builds/grafana_2.0.2_amd64.deb  
run apt-get install -y adduser libfontconfig  
run dpkg -i grafana_2.0.2_amd64.deb  
run rm grafana_2.0.2_amd64.deb  
  
# Add graphite webapp config  
add ./initial_data.json /var/lib/graphite/webapp/graphite/initial_data.json  
add ./local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py  
run cd /var/lib/graphite/webapp/graphite && python manage.py syncdb \--noinput  
# Add system service config  
add ./nginx.conf /etc/nginx/nginx.conf  
add ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add graphite carbon config  
add ./carbon.conf /var/lib/graphite/conf/carbon.conf  
add ./storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf  
run cp -r /var/lib/graphite/conf/ /graphite_conf/  
add ./startup.sh /startup.sh  
run mkdir -p /var/lib/graphite/storage/whisper  
run touch /var/lib/graphite/storage/graphite.db
/var/lib/graphite/storage/index  
run chown -R www-data /var/lib/graphite/storage  
run chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper  
run chmod 0664 /var/lib/graphite/storage/graphite.db  
# Add grafana config  
add ./grafana-defaults.ini /usr/share/grafana/conf/defaults.ini  
  
# Nginx  
expose :80  
# Carbon line receiver port  
expose :2003  
# Carbon pickle receiver port  
expose :2004  
# Carbon cache query port  
expose :7002  
# Grafana  
expose :3000  
  
VOLUME ["/usr/share/grafana/data"]  
VOLUME ["/var/lib/graphite/storage/whisper"]  
VOLUME ["/var/lib/graphite/conf/"]  
  
  
cmd ["/usr/bin/supervisord"]  
  
# vim:ts=8:noet:  

