FROM heremedia/acquia-base  
MAINTAINER Nicholas Alipaz <nicholas.alipaz@heremedia.com>  
  
COPY container /  
USER root  
  
ENV PERCONA_MAJOR_VERSION 5.5  
ENV PERCONA_MINOR_VERSION 24  
ENV PERCONA_RELEASE_VERSION 26.0  
ENV PERCONA_USER mysql  
ENV PERCONA_UID 3306  
ENV GOSU_VERSION 1.7  
RUN groupadd -r -g ${PERCONA_UID} ${PERCONA_USER} &&\  
useradd -r -u ${PERCONA_UID} -g ${PERCONA_USER} ${PERCONA_USER}  
  
RUN curl -sSL -o /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" &&\  
curl -sSL -o /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" &&\  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 &&\  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu &&\  
rm -r "$(mktemp -d)" /usr/local/bin/gosu.asc &&\  
chmod +x /usr/local/bin/gosu &&\  
gosu nobody true  
  
RUN cd /tmp/percona &&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/libmysqlclient-
dev_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/libmysqlclient18-dev_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/libmysqlclient18_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
client-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
client_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
common-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
server-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
server_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
curl -sSLO https://www.percona.com/downloads/Percona-
Server-${PERCONA_MAJOR_VERSION}/Percona-
Server-${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-${PERCONA_RELEASE_VERSION}/deb/precise/x86_64/percona-
server-
test-${PERCONA_MAJOR_VERSION}_${PERCONA_MAJOR_VERSION}.${PERCONA_MINOR_VERSION}-rel${PERCONA_RELEASE_VERSION}-256.precise_amd64.deb
&&\  
{ \  
echo percona-server-server-$PERCONA_MAJOR percona-server-server/root_password
password 'unused'; \  
echo percona-server-server-$PERCONA_MAJOR percona-server-
server/root_password_again password 'unused'; \  
} | debconf-set-selections &&\  
dpkg -i *.deb &&\  
cd / &&\  
rm -rf /tmp/percona  
  
RUN rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql &&\  
chown -R ${PERCONA_USER}:${PERCONA_USER} /var/lib/mysql /var/run/mysqld
/mnt/tmp/mysql &&\  
chmod 777 /var/run/mysqld  
  
EXPOSE 3306  
WORKDIR /  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["mysqld"]  
VOLUME ["/var/lib/mysql", "/var/log/mysql"]  

