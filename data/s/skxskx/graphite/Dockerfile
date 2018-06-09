#  
# Build it:  
# $ sudo docker build -t skxskx/graphite .  
#  
# Then launch it:  
# $ sudo docker run -d -p 5080:80 -p 7003:2003 -p 7004:2004 -p 13002:7002
skxskx/graphite  
#  
#  
# This forwards numerous ports:  
#  
# localhost:5080 -> :80 -> Graphite interface  
# localhost:7003 -> :2003 -> the carbon-cache line receiver  
# localhost:7004 -> :2004 -> the carbon-cache pickle receiver  
# localhost:12002 -> :7002 -> the carbon-cache query port  
#  
# If you're just sending data nad looking at the pretty graphs you'll be OK to  
# just forward the first two:  
#  
# $ sudo docker run -d -p 5080:80 -p 7003:2003 skxskx/graphite  
#  
# Test sending data via:  
#  
# $ echo "steve.level 3 $(date +%s)" | nc localhost 7003 --send-only  
#  
#  
# The starting point + maintainer.  
#  
from ubuntu:12.04  
MAINTAINER steve@steve.org.uk  
  
#  
# Just in case we need to get stuff installed that will prompt  
#  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Ensure we're current  
#  
run echo 'deb http://us.archive.ubuntu.com/ubuntu/ precise universe' >>
/etc/apt/sources.list  
run apt-get -y update  
  
#  
# Install required system packages  
#  
run apt-get -y install python-ldap python-cairo python-django python-twisted
python-django-tagging python-simplejson python-memcache python-pysqlite2
python-support python-pip gunicorn supervisor nginx-light  
  
#  
# Install Python stuff.  
#  
run pip install whisper  
run pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/lib" carbon  
run pip install --install-option="--prefix=/var/lib/graphite" \--install-
option="--install-lib=/var/lib/graphite/webapp" graphite-web  
  
#  
# Add system service config  
#  
add ./nginx.conf /etc/nginx/nginx.conf  
add ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#  
# Add graphite config  
#  
add ./initial_data.json /var/lib/graphite/webapp/graphite/initial_data.json  
add ./local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py  
add ./carbon.conf /var/lib/graphite/conf/carbon.conf  
add ./storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf  
  
#  
# Ensure we have a storage area, etc.  
#  
run mkdir -p /var/lib/graphite/storage/whisper  
run touch /var/lib/graphite/storage/graphite.db
/var/lib/graphite/storage/index  
run chown -R www-data /var/lib/graphite/storage  
run chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper  
run chmod 0664 /var/lib/graphite/storage/graphite.db  
run cd /var/lib/graphite/webapp/graphite && python manage.py syncdb --noinput  
  
#  
# Expose Nginx  
#  
expose :80  
#  
# Expose the carbon line-receiver port  
#  
expose :2003  
#  
# Expose the carbon pickle-receiver port  
expose :2004  
#  
# Expose the carbon cache-query port  
#  
expose :7002  
#  
# All systems go.  
#  
cmd ["/usr/bin/supervisord"]  

