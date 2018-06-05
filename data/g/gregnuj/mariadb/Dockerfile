FROM mariadb:10.2  
  
LABEL MAINTAINER="Greg Junge <gregnuj@gmail.com>"  
  
RUN set -e \  
&& apt-get update \  
&& apt-get install -y \  
\--no-install-recommends \  
\--no-install-suggests \  
dnsutils curl vim socat \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /etc/initdb.d \  
&& mkdir -p /etc/mysql/conf.d \  
&& chown -R mysql:mysql /etc/mysql \  
&& chown -R mysql:mysql /etc/initdb.d \  
&& chown -R mysql:mysql /var/lib/mysql \  
&& rm -rf /docker-entrypoint* \  
&& sed -ie 's/docker-entrypoint-initdb.d/etc\/initdb.d/'
/usr/local/bin/docker-entrypoint.sh  
  
# we expose all Cluster related Ports  
# 3306: default MySQL/MariaDB listening port  
# 4444: for State Snapshot Transfers  
# 4567: Galera Cluster Replication  
# 4568: Incremental State Transfer  
EXPOSE 3306 4444 4567 4567/udp 4568  
  
# create rsync_wan sst method  
RUN cp -p /usr/bin/wsrep_sst_rsync /usr/bin/wsrep_sst_rsync_wan  
  
COPY rootfs/ /  
  
ENTRYPOINT ["/usr/local/bin/mariadb-entrypoint.sh"]  
CMD ["mysqld"]  

