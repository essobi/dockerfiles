# Glastopf Dockerfile by MO  
#  
# VERSION 16.10  
FROM ubuntu:16.04  
MAINTAINER MO  
  
# Include dist  
ADD dist/ /root/dist/  
  
# Setup apt  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty main
restricted universe multiverse' /etc/apt/sources.list && \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main
restricted universe multiverse' /etc/apt/sources.list && \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main
restricted universe multiverse' /etc/apt/sources.list && \  
sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main
restricted universe multiverse' /etc/apt/sources.list && \  
  
apt-get update -y && \  
apt-get upgrade -y && \  
  
# Install packages  
apt-get install -y \  
build-essential \  
g++ \  
gfortran \  
git \  
libevent-dev \  
liblapack-dev \  
libmysqlclient-dev \  
libxml2-dev \  
libxslt-dev \  
make \  
python-beautifulsoup \  
python-chardet \  
python-dev \  
python-gevent \  
python-lxml \  
python-openssl \  
python-pip \  
python-requests \  
python-setuptools \  
python-sqlalchemy \  
python-mysqldb \  
cython \  
python-dateutil \  
python2.7 \  
python2.7-dev \  
supervisor \  
php7.0 \  
php7.0-dev \  
  
# Setup ewsposter  
python-mysqldb python-requests && \  
git clone https://github.com/rep/hpfeeds.git /opt/hpfeeds && \  
cd /opt/hpfeeds && \  
python setup.py install && \  
git clone https://github.com/vorband/ewsposter.git /opt/ewsposter && \  
mkdir -p /opt/ewsposter/spool /opt/ewsposter/log && \  
  
# Install php sandbox from git  
git clone https://github.com/glastopf/BFR.git /opt/BFR && \  
cd /opt/BFR && \  
phpize7.0 && \  
./configure --enable-bfr && \  
make && \  
make install && \  
make clean && \  
cd / && \  
rm -rf /opt/BFR /tmp/* /var/tmp/* && \  
echo "zend_extension = "$(find /usr -name bfr.so) >> /etc/php/7.0/cli/php.ini
&& \  
  
# Install glastopf from git  
git clone https://github.com/mushorg/glastopf.git /opt/glastopf && \  
cd /opt/glastopf && \  
python setup.py install && \  
cd / && \  
rm -rf /opt/glastopf /tmp/* /var/tmp/* && \  
  
# Setup user  
addgroup --gid 2000 tpot && \  
adduser --system \--no-create-home --shell /bin/bash --uid 2000 \--disabled-
password --disabled-login --gid 2000 tpot && \  
  
# Clean up  
apt-get purge -y build-essential make git g++ php7.0 php7.0-dev && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
# Add configs  
mkdir -p /opt/glastopf && \  
mv /root/dist/glastopf.cfg /opt/glastopf/ && \  
mv /root/dist/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Set workdir and start glastopf  
WORKDIR /data/glastopf/  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  

