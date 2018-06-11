FROM debian:jessie  
MAINTAINER Ovais Tariq @ovaistariq  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PERCONA_MAJOR 5.7  
ENV PERCONA_VERSION 5.7.16-27.19-1.jessie  
  
RUN apt-get update && apt-get install -y --force-yes \  
wget  
  
RUN wget https://repo.percona.com/apt/percona-release_0.1-4.jessie_all.deb \  
&& dpkg -i percona-release_0.1-4.jessie_all.deb  
  
RUN apt-get update && apt-get install -y --force-yes \  
apt-transport-https ca-certificates \  
percona-xtradb-cluster-57 \  
curl pwgen jq  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql \  
&& chown mysql:mysql /var/lib/mysql  
  
COPY my.cnf /etc/mysql/my.cnf  
COPY entrypoint.sh /entrypoint.sh  
COPY clustercheckcron /usr/bin/clustercheckcron  
  
RUN chmod a+x /usr/bin/clustercheckcron  
  
# All this must be overwritten at runtime  
ENV CLUSTER_NAME PXC  
ENV MYSQL_DATABASE twindb  
ENV MYSQL_USER twindb  
ENV MYSQL_PASSWORD twindb  
ENV XTRABACKUP_PASSWORD xtrabackup  
  
VOLUME /var/lib/mysql  
VOLUME /var/log/mysql  
  
EXPOSE 3306  
EXPOSE 4567  
EXPOSE 4568  
LABEL vendor=Percona  
LABEL com.percona.package="Percona XtraDB Cluster"  
LABEL com.percona.version="5.7"  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD [""]  

