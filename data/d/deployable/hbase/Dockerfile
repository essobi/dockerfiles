FROM openjdk:8-jre  
  
RUN set -uex; \  
echo 'precedence ::ffff:0:0/96 100' >> /etc/gai.conf; \  
apt-get update; \  
apt-get install netcat-openbsd wget ca-certificates xxd -y; \  
apt-get clean  
  
# gpg key servers can be flakey :/  
RUN set -uex; \  
for key in \  
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
73855CE2D0A67B5A \  
461D2D1B577F40C58EC2FE060CF65F72E4609424 \  
6370E6D65FE1D8437C4CF905A6ECA8953B417B9B; \  
do \  
echo $key; \  
gpg --keyserver keys.gnupg.net --recv-keys $key \  
|| gpg --keyserver pgp.mit.edu --recv-keys $key \  
|| gpg --keyserver ha.pool.sks-keyservers.net --recv-keys $key; \  
done  
  
ENV GOSU_VERSION 1.10  
RUN set -uex; \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu --progress=dot:giga \  
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc --progress=dot:giga \  
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -f /usr/local/bin/gosu.asc; \  
chmod +x /usr/local/bin/gosu; \  
gosu nobody true  
  
ARG APACHE_PROJECT_LABEL=hbase  
ARG APACHE_PROJECT_VERSION=1.4.1  
ARG APACHE_PROJECT_LABEL_VERSION=hbase-1.4.1  
ARG APACHE_PROJECT_RELEASE_FILE=hbase-1.4.1-bin.tar.gz  
  
RUN set -uex; \  
mkdir -p -m 700 /install/gpg; \  
cd /install; \  
wget https://www-us.apache.org/dist/${APACHE_PROJECT_LABEL}/KEYS; \  
gpg --import KEYS; \  
wget --progress=dot https://www-
us.apache.org/dist/${APACHE_PROJECT_LABEL}/${APACHE_PROJECT_VERSION}/${APACHE_PROJECT_RELEASE_FILE}.asc;
\  
wget --progress=dot:giga
http://mirrors.gigenet.com/apache/${APACHE_PROJECT_LABEL}/${APACHE_PROJECT_VERSION}/${APACHE_PROJECT_RELEASE_FILE};
\  
gpg --batch --verify ${APACHE_PROJECT_RELEASE_FILE}.asc
${APACHE_PROJECT_RELEASE_FILE}; \  
tar -xzf ${APACHE_PROJECT_RELEASE_FILE}; \  
mv ${APACHE_PROJECT_LABEL_VERSION} /${APACHE_PROJECT_LABEL}; \  
rm -rf /install  
  
# server.properties zookeeper.properties log4j.properties  
COPY ./hbase-site.xml /hbase/conf/  
COPY docker-entrypoint.sh /entrypoint.sh  
#COPY check.sh /hbase/check.sh  
RUN set -uex; \  
useradd hbase -r -s /bin/false -u 20030; \  
mkdir -p /${APACHE_PROJECT_LABEL}/logs; \  
mkdir -p /data/hbase; \  
mkdir -p /data/zookeeper; \  
chown -R hbase:hbase /hbase/logs /data  
  
# gosu user hbase  
VOLUME [ "/hbase/logs", "/data" ]  
WORKDIR /hbase  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["hbase"]  
  

