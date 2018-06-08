FROM phusion/baseimage:0.9.20  
  
MAINTAINER moltar <moltar@moltar.net>  
  
EXPOSE 4730  
  
RUN apt-get update -qq && \  
apt-get install -y gcc make g++ libboost-all-dev gperf libevent-dev \  
uuid-dev libmysqld-dev libpq-dev libsqlite3-dev libhiredis-dev \  
unzip && \  
curl -L \--silent -o /tmp/cyassl.zip http://www.yassl.com/cyassl-3.2.0.zip &&
\  
cd /tmp && \  
unzip -qq cyassl.zip && \  
cd cyassl* && \  
./configure \  
\--prefix=/usr && \  
make && \  
make install && \  
mkdir /tmp/gearman && \  
curl -L \--insecure \--silent
https://github.com/gearman/gearmand/releases/download/1.1.15/gearmand-1.1.15.tar.gz
\  
| tar -xz \--strip 1 -C /tmp/gearman && \  
cd /tmp/gearman && \  
./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--enable-hiredis && \  
make && \  
make install && \  
adduser \--system \--no-create-home \--disabled-login \--disabled-password
\--group gearman && \  
apt-get purge -y gcc make gperf libevent-dev uuid-dev \  
libmysqld-dev libpq-dev libsqlite3-dev libhiredis-dev unzip && \  
apt-get autoremove -y && \  
apt-get install -y telnet libmysqlclient20 libhiredis0.13 libevent-2.0-5
libpq5 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/sbin/my_init", "--", "/usr/sbin/gearmand", "--log-file=stderr",
"--user=gearman"]  

