FROM ubuntu:14.04  
MAINTAINER Keri Alleyne <info@symlogix.com>  
#ENV HOME /root  
RUN apt-get update && apt-get install -y \  
avahi-daemon \  
build-essential \  
curl \  
libacl1-dev \  
libavahi-client-dev \  
libcrack2-dev \  
libdb-dev \  
libdbus-1-dev \  
libdbus-glib-1-dev \  
libevent-dev \  
libgcrypt-dev \  
libglib2.0-dev \  
libkrb5-dev \  
libldap2-dev \  
libmysqlclient-dev \  
libpam0g-dev \  
libssl-dev \  
libtdb-dev \  
libtracker-miner-0.16-dev \  
libtracker-sparql-0.16-dev \  
libwrap0-dev \  
make \  
nano \  
systemtap-sdt-dev \  
tracker  
RUN mkdir -p /IMG \  
&& curl -SL
http://sourceforge.net/projects/netatalk/files/netatalk/3.1.8/netatalk-3.1.8.tar.bz2
\  
| tar -xjC /IMG  
RUN cd /IMG/netatalk-3.1.8 \  
&& ./configure \  
\--with-init-style=debian-sysv \  
\--without-libevent \  
\--without-tdb \  
\--with-cracklib \  
\--enable-krbV-uam \  
\--with-pam-confdir=/etc/pam.d \  
\--with-dbus-sysconf-dir=/etc/dbus-1/system.d \  
\--with-tracker-pkgconfig-version=0.16  
RUN cd /IMG/netatalk-3.1.8 \  
&& make \  
&& make install  
EXPOSE 548 5353  

