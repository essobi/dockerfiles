FROM ubuntu:16.04  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
# curl \  
# cython \  
# git \  
# haproxy\  
# jsonlint \  
libapache2-mod-php \  
libapache2-mod-wsgi \  
# libconfig-file-perl \  
# libhashkit-dev \  
# libhashkit2 \  
libmemcached-dev \  
libmemcached11 \  
python2.7 \  
python-beaker \  
python-bottle \  
python-crypto \  
python-dateutil \  
python-dev \  
python-httplib2 \  
python-ipaddr \  
python-lockfile \  
python-memcache \  
python-mysqldb \  
python-netaddr \  
python-nose \  
python-nosexcover \  
python-paramiko \  
python-pexpect \  
python-pip \  
python-pycurl \  
python-requests \  
python-simplejson \  
python-sqlalchemy \  
# python-sqlite \  
python-urllib3 \  
libxml2-dev \  
libxslt1-dev \  
git \  
python-zc.lockfile \  
ansible  
  
RUN a2enmod wsgi && a2enmod ssl  
  
RUN pip install --upgrade pip && pip install Beaker==1.6.4 \  
bottle==0.12.7 \  
chardet==2.3.0 \  
coverage==3.7.1 \  
crontab==0.21.3 \  
cryptography==1.2.3 \  
Django==1.11.4 \  
django-filter==0.8 \  
django-tools==0.31.0 \  
djangorestframework==3.6.4 \  
ecdsa==0.13 \  
enum34==1.1.2 \  
httplib2==0.9.1 \  
idna==2.0 \  
ipaddr==2.1.11 \  
ipaddress==1.0.16 \  
lockfile==0.12.2 \  
ndg-httpsclient==0.4.0 \  
netaddr==0.7.18 \  
nose==1.3.7 \  
nosexcover==1.0.10 \  
paramiko==1.16.0 \  
pbkdf2==1.3 \  
pexpect==4.0.1 \  
ptyprocess==0.5 \  
pwgen==0.8.2.post0 \  
py-bcrypt==0.4 \  
pyasn1==0.1.9 \  
pycurl==7.43.0 \  
pyOpenSSL==0.15.1 \  
python-dateutil==2.4.2 \  
python-memcached==1.53 \  
pyvmomi==6.5.0.2017.5.post1 \  
requests==2.9.1 \  
simplejson==3.8.1 \  
six==1.10.0 \  
SQLAlchemy==1.0.11 \  
urllib3==1.13.1 \  
zc.lockfile==1.0.2 \  
django-admin-tools \  
docutils \  
django-suit \  
pycrypto \  
mysqlclient \  
django-logentry-admin \  
django_select2 \  
gunicorn==19.7.1 \  
Celery \  
django_celery_results \  
redis \  
flower  
  
RUN mkdir /var/log/stackscale && chmod 777 /var/log/stackscale  
  
ENTRYPOINT ["apache2ctl", "-D", "FOREGROUND"]  

