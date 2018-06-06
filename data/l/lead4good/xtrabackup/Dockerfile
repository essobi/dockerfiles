FROM debian:jessie  
  
RUN \  
echo "deb http://repo.percona.com/apt jessie main" >
/etc/apt/sources.list.d/percona-release.list \  
&& apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
9334A25F8507EFA5 \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
percona-xtrabackup-24 percona-toolkit qpress bash \  
&& mkdir -p /backups && mkdir -p /var/lib/mysql \  
&& apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
# Allow mountable backup path  
VOLUME ["/backups"]  
  
# Copy the script to simplify backup command  
COPY backup.sh /backup.sh  
COPY xtrabackup.sh /xtrabackup.sh  

