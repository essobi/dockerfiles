FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends software-properties-common ca-
certificates wget openssl rsync lsof  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv BC19DDBA  
RUN add-apt-repository 'deb http://releases.galeracluster.com/galera-3/ubuntu
xenial main'  
RUN add-apt-repository 'deb http://releases.galeracluster.com/mysql-
wsrep-5.7/ubuntu xenial main'  
  
RUN apt-get update  
RUN apt-get install -y galera-3 galera-arbitrator-3 mysql-wsrep-5.7 && rm -rf
/var/lib/apt/lists/*  
  
ENV GOSU_VERSION 1.7  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
RUN mkdir -p /var/run/mysqld && chown mysql:mysql /var/run/mysqld  
  
ADD https://github.com/ufoscout/docker-compose-
wait/releases/download/2.2.1/wait /wait  
RUN chmod +x /wait  
  
COPY galera-entrypoint.sh /  
RUN chmod +x /galera-entrypoint.sh  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 3306 4444 4567 4567/udp 4568  
ENV MYSQL_INITDB_SKIP_TZINFO 1  
ENTRYPOINT ["/galera-entrypoint.sh"]  
CMD ["mysqld"]  

