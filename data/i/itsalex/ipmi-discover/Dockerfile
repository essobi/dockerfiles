FROM ubuntu:16.04 AS build  
  
ENV LANG C.UTF-8  
ENV KEA_VERSION 1.3.0  
  
RUN apt update && apt -y --no-install-recommends --no-upgrade install \  
# Build deps  
make \  
automake \  
g++ \  
dh-autoreconf \  
# Tools deps  
unzip \  
wget \  
# kea deps  
libtool \  
autoconf \  
libssl-dev \  
liblog4cplus-dev \  
libboost-system-dev \  
libpq-dev \  
postgresql-server-dev-all \  
## build kea  
&& cd / \  
&& wget -O kea.tar.gz --no-check-certificate
https://ftp.isc.org/isc/kea/$KEA_VERSION/kea-$KEA_VERSION.tar.gz \  
&& mkdir -p /usr/src/kea \  
&& tar xf kea.tar.gz --strip-components=1 -C /usr/src/kea \  
&& rm kea.tar.gz \  
&& cd /usr/src/kea \  
&& autoreconf \  
\--install \  
&& CXXFLAGS='-Os' ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--with-log4cplus \  
\--with-dhcp-pgsql \  
\--with-openssl \  
\--enable-static=false \  
&& make -j "$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
## cleanup  
&& rm -rf /usr/src \  
&& apt purge -y --allow-remove-essential \  
make \  
automake \  
g++ \  
dh-autoreconf \  
unzip \  
wget \  
libtool \  
autoconf \  
libssl-dev \  
liblog4cplus-dev \  
e2fslibs \  
postgresql-server-dev-all \  
&& apt remove --purge -y --allow-remove-essential $(apt-mark showauto) \  
&& apt autoremove -y \  
&& apt install -y --no-install-recommends --no-upgrade \  
freeipmi-tools \  
liblog4cplus-dev \  
libboost-system-dev \  
libpq-dev \  
python3 \  
python3-pip \  
python3-setuptools \  
python3-wheel  
  
WORKDIR /code/  
  
COPY setup.py /code/  
COPY ipmi_finder /code/  
COPY launch-services.sh /launch-services.sh  
  
RUN pip3 install -e /code/ \  
&& chmod o+rx /launch-services.sh  
  
EXPOSE 67/udp  
  
CMD ["/launch-services.sh"]  

