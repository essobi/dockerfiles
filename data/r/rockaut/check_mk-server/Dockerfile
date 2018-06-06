FROM ubuntu:xenial  
LABEL maintainer "rockaut" <fischbacher.markus@gmail.com>  
EXPOSE 5000  
# Install prequesites  
RUN apt-get update && apt-get install -y wget curl time traceroute libsnmp-
python dialog dnsutils \  
fping graphviz libapache2-mod-fcgid apache2 apache2-utils libdbi1
libevent-1.4-2 libltdl7 \  
libnet-snmp-perl libpango1.0-0 libperl5.22 libreadline5 libsnmp-perl libuuid1
libxml2 patch \  
php-cli php-cgi php-gd php-mcrypt php-sqlite3 php-json php-pear pyro rsync
smbclient rpcbind \  
snmp unzip xinetd python-ldap freeradius-utils libpcap0.8 rpm binutils lcab
libgsf-1-114 libglib2.0-0 \  
python-reportlab python-imaging poppler-utils python-openssl \  
iputils-arping iputils-clockdiff iputils-ping iputils-tracepath libgnutls-
openssl27 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# install check_mk and dependents  
ARG CMK_VERSION=1.2.8p19  
  
RUN wget "https://mathias-kettner.de/support/${CMK_VERSION}/check-mk-
raw-${CMK_VERSION}_0.xenial_amd64.deb" \  
&& dpkg -i check-mk-raw-${CMK_VERSION}_0.xenial_amd64.deb || true \  
&& apt-get install -y -f \  
&& rm -f /*.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# create site and set defaults  
ARG sitename=cmk  
  
RUN omd create ${sitename}; \  
omd config ${sitename} set APACHE_TCP_ADDR 0.0.0.0; \  
omd config ${sitename} set DEFAULT_GUI check_mk; \  
omd config ${sitename} set TMPFS off;  
  
# copy startscript and tools  
COPY ./start.sh /usr/local/bin/start.sh  
COPY ./auth.serials /opt/omd/sites/${sitename}/etc/auth.serials  
  
VOLUME [ "/opt/omd/sites/${sitename}/local",
"/opt/omd/sites/${sitename}/etc/check_mk" ]  
  
# finish  
CMD bash -C '/usr/local/bin/start.sh';'/bin/bash'  

