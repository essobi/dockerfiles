#  
# Carto API container  
#  
FROM phusion/baseimage:0.9.18  
MAINTAINER Volkan Unsal <spocksplanet@gmail.com>  
  
# Configuring locales  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update &&\  
apt-get install -y -q \  
build-essential \  
autoconf \  
automake \  
libtool \  
checkinstall \  
unp \  
zip \  
unzip \  
git-core \  
git \  
curl \  
ca-certificates \  
openssl \  
python2.7-dev \  
python-setuptools \  
python-gdal \  
gdal-bin \  
\--no-install-recommends  
  
RUN git config --global user.email spocksplanet@gmail.com \  
&& git config --global user.name "Volkan Unsal"  
  
# ogr2ogr2 static build, see https://github.com/CartoDB/cartodb/wiki/How-to-
build-gdal-and-ogr2ogr2  
RUN git clone https://github.com/OSGeo/gdal /opt/ogr2ogr2  
WORKDIR /opt/ogr2ogr2  
RUN git remote add cartodb https://github.com/cartodb/gdal \  
&& git fetch cartodb \  
&& git checkout trunk \  
&& git pull origin trunk \  
&& git checkout upstream \  
&& git merge -s ours --ff-only origin/trunk \  
&& git checkout ogr2ogr2 \  
&& git merge -s ours upstream -m "Merged it" \  
&& cd ogr2ogr2 \  
&& ./configure --disable-shared \  
&& make -j 4 \  
&& cp ./apps/ogr2ogr /usr/bin/ogr2ogr2 \  
&& rm -rf /opt/ogr2ogr2 /root/.gitconfig  
  
# Install NodeJS  
RUN curl
https://nodejs.org/download/release/v0.10.41/node-v0.10.41-linux-x64.tar.gz|
tar -zxf - --strip-components=1 -C /usr  
  
# Install postgres-client and libpq-dev (required by
https://github.com/CartoDB/node-postgres/blob/cdb-2.6/binding.gyp)  
RUN apt-get update &&\  
apt-get install -y -q \  
postgresql-9.3 \  
libpq-dev  
  
# Install SQL API  
RUN git clone https://github.com/CartoDB/CartoDB-SQL-API /CartoDB-SQL-API  
WORKDIR /CartoDB-SQL-API  
RUN git reset --hard 5d8aa635030a18437114019a9be36fa395f1e991 \  
&& ./configure \  
&& npm install  
  
# Assume the following linked services  
# - postgres:5432  
# - redis:6379  
# - statsd:8125  
# Import configurations  
COPY ./config/CartoDB-dev.js \  
/CartoDB-SQL-API/config/environments/development.js  
  
EXPOSE 8080  
# runit entries. These are scripts to run as daemons after bootup.  
# RUN mkdir /etc/service/node  
# ADD ./daemons/node.sh /etc/service/node/run  
# Scripts  
RUN mkdir -p /etc/my_init.d  
ADD my_init.d/* /etc/my_init.d/  
  
CMD ["/sbin/my_init"]  
  
ENV GDAL_DATA /usr/share/gdal/1.10  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

