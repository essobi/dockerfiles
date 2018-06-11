FROM debian:9  
RUN groupadd zabbix && useradd -g zabbix zabbix && \  
apt-get update && apt-get install -y --no-install-recommends gcc make
libgnutls28-dev proot curl libevent-dev libpcre3-dev && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
ARG ZBX_VERSION=3.4.10  
WORKDIR /usr/src  
RUN curl -L --output /usr/src/zabbix.tar.gz
http://ufpr.dl.sourceforge.net/project/zabbix/ZABBIX%20Latest%20Stable/${ZBX_VERSION}/zabbix-${ZBX_VERSION}.tar.gz  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /usr/local/bin/dumb-init  
  
RUN chmod +x /usr/local/bin/dumb-init && \  
tar xzvf zabbix.tar.gz && \  
cd /usr/src/zabbix-$ZBX_VERSION && \  
./configure --enable-agent --with-gnutls && \  
make -j && make install && \  
rm -rf /usr/src/zabbix.tar.gz  
  
RUN chown -R zabbix:zabbix /usr/local/etc/zabbix_agentd.conf.d && \  
echo "Include=/usr/local/etc/zabbix_agentd.conf.d/" >
/usr/local/etc/zabbix_agentd.conf  
EXPOSE 10050  
COPY files/docker-entrypoint.sh /  
  
USER zabbix  
ENTRYPOINT ["/usr/local/bin/dumb-init","/docker-entrypoint.sh"]  

