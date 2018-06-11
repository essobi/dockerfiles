FROM debian:9  
COPY files/sources.list /etc/apt/sources.list  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /usr/local/bin/dumb-init  
  
RUN groupadd zabbix && useradd -g zabbix zabbix && \  
chmod +x /usr/local/bin/dumb-init && \  
apt-get update && apt-get -y install --no-install-recommends fping wget tar
gcc curl make \  
libssh2-1-dev libsqlite3-dev libldap2-dev libiksemel-dev libopenipmi-dev
unixodbc-dev libsnmp-dev snmp libpng-dev \  
libxml2-dev libgnutls28-dev libcurl4-gnutls-dev git nmap fping traceroute
libldb-dev libevent-dev libpcre3-dev && \  
ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
WORKDIR /usr/src  
ARG ZBX_VERSION=3.4.10  
RUN curl -L --output /usr/src/zabbix.tar.gz
http://ufpr.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/${ZBX_VERSION}/zabbix-${ZBX_VERSION}.tar.gz  
  
RUN git -c http.SslVerify=False clone https://github.com/meduketto/iksemel.git
&& \  
tar xzvf zabbix.tar.gz && \  
cd /usr/src/zabbix-$ZBX_VERSION && \  
./configure --enable-proxy --enable-agent --with-sqlite3 \  
\--with-net-snmp --with-libcurl --with-openipmi --with-gnutls \  
\--with-ldap --with-libcurl --with-ssh2 --with-unixodbc \  
\--with-jabber=/usr/src/iksemel --with-libxml2 && make -j && make install -j
&& \  
rm -rf /usr/src/*  
  
RUN chown -R zabbix:zabbix /usr/local/etc && \  
ln -s /usr/bin/fping /usr/sbin/fping  
  
EXPOSE 10051  
COPY files/docker-entrypoint.sh /  
  
USER zabbix  
ENTRYPOINT ["/usr/local/bin/dumb-init","/docker-entrypoint.sh"]  

