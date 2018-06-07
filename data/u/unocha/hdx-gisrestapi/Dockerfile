FROM phusion/baseimage:0.9.18  
  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /srv/gisapi  
  
COPY . .  
  
# libc-bin and ubuntu-toolchain/test is added BECAUSE OF "Error:
/usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.20' not found
(required by /srv/gisapi/node_modules/mapnik/lib/binding/mapnik.node)"  
  
RUN echo -en
"LANGUAGE=en_US.UTF-8\nLC_ALL=en_US.UTF-8\nLC_PAPER=en_US.UTF-8\nLC_ADDRESS=en_US.UTF-8\n"
> /etc/default/locale && \  
echo -en
"LC_MONETARY=en_US.UTF-8\nLC_NUMERIC=en_US.UTF-8\nLC_TELEPHONE=en_US.UTF-8\nLC_IDENTIFICATION=en_US.UTF-8\n"
>> /etc/default/locale && \  
echo -en
"LC_MEASUREMENT=en_US.UTF-8\nLC_TIME=en_US.UTF-8\nLC_NAME=en_US.UTF-8\nLANG=en_US.UTF-8"
>> /etc/default/locale && \  
locale-gen en_US.UTF-8 && dpkg-reconfigure locales && \  
apt-get -qq update && \  
apt-get -qq -y dist-upgrade && \  
apt-get -qq -y install \  
gettext-base \  
mc \  
msmtp \  
nano \  
telnet \  
python-software-properties \  
software-properties-common \  
git \  
build-essential && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get -qq -y
install nodejs && \  
mkdir -p /etc/service/gisapi /srv && \  
mv docker/run_gisapi /etc/service/gisapi/run && \  
chmod +x /etc/service/gisapi/run && \  
add-apt-repository -y ppa:mapnik/nightly-2.3 && \  
apt-get -qq -y update && \  
apt-get -qq -y install gdal-bin \  
postgresql-client \  
libmapnik \  
libmapnik-dev \  
mapnik-utils \  
python-mapnik \  
mapnik-input-plugin-gdal && \  
apt-get -qq -y install libc-bin && \  
add-apt-repository -y ppa:ubuntu-toolchain-r/test && \  
apt-get -qq -y update && \  
apt-get -qq -y upgrade && \  
apt-get -qq -y dist-upgrade && \  
npm install && \  
npm cache clean && \  
apt-get remove -y build-essential && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

