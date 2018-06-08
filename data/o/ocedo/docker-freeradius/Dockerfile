FROM ubuntu:precise  
  
RUN apt-get update -y && apt-get -y install \  
wget build-essential net-tools tcpdump lsb-base \  
libc6 libgdbm3 libltdl7 libpam0g libperl5.14 libpython2.7 \  
libssl1.0.0 ssl-cert ca-certificates adduser libmhash-dev libtalloc-dev \  
libperl-dev libssl-dev libpam-dev libgdb-dev libgdbm-dev git-core checkinstall  
  
WORKDIR /opt  
RUN wget ftp://ftp.freeradius.org/pub/freeradius/freeradius-
server-3.0.11.tar.gz  
RUN tar -xvf freeradius-server-3.0.11.tar.gz  
  
WORKDIR /opt/freeradius-server-3.0.11  
RUN ./configure  
RUN checkinstall -y --nodoc  
  
# Until heartbleed patch makes it into repo, ignore checking  
RUN sed -i 's/allow_vulnerable_openssl.*/allow_vulnerable_openssl = yes/g' \  
/usr/local/etc/raddb/radiusd.conf  
  
ADD ./src/clients.conf /usr/local/etc/raddb/clients.conf  
ADD ./src/users /usr/local/etc/raddb/users  
  
ADD ./src/default /usr/local/etc/raddb/sites-available/default  
ADD ./src/inner-tunnel /usr/local/etc/raddb/sites-available/inner-tunnel  
  
EXPOSE 1812/udp  
EXPOSE 1813/udp  
EXPOSE 1814/udp  
EXPOSE 18120/udp  
  
CMD /usr/local/sbin/radiusd -X  

