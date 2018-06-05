FROM centos:latest  
MAINTAINER Muneeb Ahmad <beenum>  
WORKDIR /root  
EXPOSE 67/udp  
VOLUME /var/lib/kea  
RUN yum update -y && \  
yum install -y epel-release initscripts && \  
yum install -y --nogpgcheck git gcc-c++ bc make automake libtool boost boost-
devel sqlite-devel lbzip2 pkg-config openssl-devel wget postgresql-devel && \  
wget https://sourceforge.net/projects/log4cplus/files/log4cplus-
stable/1.1.3/log4cplus-1.1.3-rc7.tar.bz2 && \  
tar xf log4cplus-1.1.3-rc7.tar.bz2 && \  
cd log4cplus-1.1.3-rc7 && \  
./configure --prefix=/opt/log4cplus && \  
make && make install && \  
cd && git clone https://github.com/isc-projects/kea && \  
cd kea && \  
autoreconf --install && \  
./configure --with-dhcp-pgsql=/usr/bin/pg_config --with-boost-
include=/usr/include/ --with-log4cplus=/opt/log4cplus --prefix=/opt/kea && \  
make && make install && \  
cd && rm -rf * && \  
yum clean all  
ENTRYPOINT [ "/opt/kea/sbin/kea-dhcp4" ]  
CMD ["-c", "/opt/kea/etc/kea/kea.conf"]  

