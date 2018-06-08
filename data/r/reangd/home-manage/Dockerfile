FROM debian:jessie  
  
MAINTAINER ReanGD  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD * /home/  
  
RUN echo en_US.UTF-8 UTF-8 > /etc/locale.gen && \  
echo ru_RU.UTF-8 UTF-8 >> /etc/locale.gen && \  
\  
apt-get update && \  
apt-get install -y --no-install-recommends locales supervisor gcc git nfs-
common autofs python-minimal python-pip python-dev python-six python-
transmissionrpc python-psycopg2 nginx npm && \  
apt-get install -y --no-install-recommends vim && \  
\  
rm /etc/auto.master && \  
ln -s /home/auto.master /etc/ && \  
\  
mkdir -p /www/tmp/spooler /www/app /www/static/jquery /www/static/bootstrap
/www/static/django_ajax && \  
echo "daemon off;" >> /etc/nginx/nginx.conf && \  
rm /etc/nginx/sites-enabled/default && \  
\  
pip install -r /home/requirements.txt && \  
\  
cp /usr/local/lib/python2.7/dist-
packages/django_ajax/static/django_ajax/js/*.min.* /www/static/django_ajax &&
\  
\  
ln -s /usr/bin/nodejs /usr/bin/node && \  
npm install -g bower && \  
\  
cd /tmp && \  
bower --allow-root --config.interactive=false install --production
jquery#2.1.3 bootstrap#3.3.1 && \  
cp /tmp/bower_components/jquery/dist/*.min.* /www/static/jquery/ && \  
cp -r /tmp/bower_components/bootstrap/dist/* /www/static/bootstrap/ && \  
\  
bower --allow-root --config.interactive=false cache clean && \  
rm -rf /.cache/bower && \  
rm -rf /tmp/bower_components && \  
npm uninstall -g bower && \  
\  
apt-get --purge remove --auto-remove -y python-pip npm gcc && \  
apt-get clean && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/lib/apt/* && \  
rm -rf /var/lib/dpkg/* && \  
rm -rf /var/lib/cache/* && \  
rm -rf /var/lib/log/* && \  
rm -rf /usr/share/i18n/ && \  
rm -rf /usr/share/doc/ && \  
rm -rf /usr/share/locale/ && \  
rm -rf /usr/share/man/ && \  
rm -rf /usr/sbin/locale-gen && \  
rm -rf /usr/sbin/update-locale && \  
rm -rf /usr/sbin/validlocale  
  
ENV LANG ru_RU.UTF-8  
ENV LANGUAGE ru_RU.UTF-8  
  
EXPOSE 80/tcp  
  
VOLUME ["/www/tmp", "/www/app"]  
  
CMD /home/run.sh

