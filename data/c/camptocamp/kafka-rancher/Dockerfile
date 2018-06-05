FROM openjdk:8  
ENV CONFD_VERSION=0.12.0-alpha3 \  
KAFKA_USER=kafka \  
KAFKA_VERSION=0.10.0.1 \  
SCALA_VERSION=2.11  
# Add a user  
RUN adduser --system "$KAFKA_USER"  
  
# Install runit  
RUN apt-get update \  
&& apt-get install -y --no-install-suggests --no-install-recommends \  
runit \  
&& rm -rf /var/lib/apt/lists/*  
  
# Down confd  
RUN curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd  
  
# Download Apache Kafka, untar and cleanup  
RUN curl -L -o /kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
http://www.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
\  
&& tar -xzf kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz \  
&& chown kafka -R kafka_${SCALA_VERSION}-${KAFKA_VERSION} \  
&& ln -s kafka_${SCALA_VERSION}-${KAFKA_VERSION} kafka \  
&& rm kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz  
  
# Install Gosu  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./confd.run /etc/service/confd/run  
COPY ./kafka.run /etc/service/kafka/run  
  
COPY ./conf.d /etc/confd/conf.d  
COPY ./templates /etc/confd/templates  
  
COPY ./docker-entrypoint.sh /  
  
EXPOSE 9092  
VOLUME [ "/tmp/kafka-logs" ]  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

