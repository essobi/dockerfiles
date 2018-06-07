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
6370E6D65FE1D8437C4CF905A6ECA8953B417B9B \  
BA1CBB7D4C0D222CCF8A5C844B606607518830CF; \  
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
  
ARG KAFKA_VERSION=0.11.0.2  
ARG SCALA_VERSION=2.12  
RUN set -uex; \  
mkdir -p -m 700 /install/gpg; \  
cd /install; \  
label="kafka_${SCALA_VERSION}-${KAFKA_VERSION}"; \  
wget --progress=dot https://www-
us.apache.org/dist/kafka/$KAFKA_VERSION/$label.tgz.asc; \  
wget --progress=dot:giga
http://ftp.jaist.ac.jp/pub/apache/kafka/$KAFKA_VERSION/$label.tgz; \  
gpg --batch --verify $label.tgz.asc $label.tgz; \  
tar -xzf $label.tgz; \  
mv $label /kafka; \  
rm -rf /install  
  
# server.properties zookeeper.properties log4j.properties  
COPY ./config /kafka/config  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY check.sh /kafka/check.sh  
  
RUN set -uex; \  
useradd kafka -r -s /bin/false -u 20029; \  
mkdir -p /kafka/logs; \  
mkdir -p /data/kafka; \  
mkdir -p /data/zookeeper; \  
chown -R kafka:kafka /kafka/logs /data  
  
#USER kafka  
VOLUME [ "/kafka/logs", "/data" ]  
WORKDIR /kafka  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["kafka"]  
  

