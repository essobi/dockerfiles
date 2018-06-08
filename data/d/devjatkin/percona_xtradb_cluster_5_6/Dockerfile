FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://repo.percona.com/apt xenial main" >
/etc/apt/sources.list.d/percona.list  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends percona-xtradb-cluster-56 curl
ca-certificates \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql && chown -R mysql:mysql
/var/lib/mysql  
  
RUN curl -o kubectl https://storage.googleapis.com/kubernetes-
release/release/v1.2.4/bin/linux/amd64/kubectl  
RUN chmod +x kubectl  
  
VOLUME /var/lib/mysql  
  
COPY my.cnf /etc/mysql/my.cnf  
COPY cluster.cnf /etc/mysql/conf.d/cluster.cnf  
  
# ports: mysql state-snapshot-transfer replication-traffic incremental-state-
transfer  
EXPOSE 3306 4444 4567 4568  
COPY ./entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mysqld"]  

