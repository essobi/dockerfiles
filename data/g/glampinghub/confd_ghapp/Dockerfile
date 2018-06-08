FROM ubuntu:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive PORT=8000 ENV=develop DEBUG=True  
  
COPY ./requirements.txt /tmp/  
COPY ./docker-entrypoint.sh /  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 /usr/bin/confd  
ADD https://deb.nodesource.com/setup_5.x /tmp/setup-nodejs  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
chmod +x /usr/bin/confd && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DE742AFA && \  
bash -c 'source /etc/lsb-release; echo "deb
http://ppa.launchpad.net/maxmind/ppa/ubuntu $DISTRIB_CODENAME main" >
/etc/apt/sources.list.d/maxmind.list' && \  
bash /tmp/setup-nodejs && \  
apt-get install --no-install-recommends -qy \  
nodejs \  
libmaxminddb0 libmaxminddb-dev \  
memcached \  
python-dev \  
python-pip \  
libjpeg8 libjpeg8-dev libtiff5 libtiff5-dev libfreetype6 libfreetype6-dev \  
libgeos-3.4.2 libgeos-dev gdal-bin libgdal-dev python-gdal binutils libproj-
dev gdal-bin \  
gunicorn \  
celeryd \  
supervisor \  
xtail \  
git \  
libpq-dev \  
build-essential \  
vim && \  
apt-get purge -qy python-librabbitmq librabbitmq1 && \  
ln -s /usr/include/freetype2 /usr/local/include/freetype && \  
npm install --global \--production bower gulp && \  
mkdir -p /webapp/dist /webapp/src && \  
pip install -r /tmp/requirements.txt && \  
useradd -u 999 -s /usr/sbin/nologin -r -M -d /nonexistent webapp && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && npm cache
clean  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["ghapp"]  

