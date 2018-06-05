FROM phusion/baseimage  
MAINTAINER Laur  
# https://manual.seafile.com/deploy/using_sqlite.html  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Seafile dependencies and system configuration  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y \  
python2.7 \  
libpython2.7 \  
python-setuptools \  
python-imaging \  
python-mysqldb \  
python-urllib3 \  
python-memcache \  
wget \  
crudini \  
unattended-upgrades  
RUN update-locale LANG=C.UTF-8  
  
# deps for pylibmc:  
RUN apt-get install --no-install-recommends -y \  
python-pip \  
libmemcached-dev \  
zlib1g-dev \  
python-dev \  
build-essential  
  
RUN pip install pylibmc django-pylibmc  
  
RUN ulimit -n 30000  
  
EXPOSE 10001 12001 8000 8080 8082  
# Baseimage init process  
ENTRYPOINT ["/sbin/my_init"]  
  
# Seafile daemons  
RUN mkdir /etc/service/seafile /etc/service/seahub  
ADD seafile.sh /etc/service/seafile/run  
ADD seahub.sh /etc/service/seahub/run  
  
ADD setup-seafile.sh /usr/local/sbin/setup-seafile  
ADD apt-auto-upgrades /etc/apt/apt.conf.d/20auto-upgrades  
  
# Clean up for smaller image  
RUN apt-get purge -y \  
python-pip \  
zlib1g-dev \  
python-dev \  
build-essential  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR "/seafile"  

