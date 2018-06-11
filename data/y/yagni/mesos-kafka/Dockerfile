FROM debian:8.3  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV JAVA_VERSION 8  
ENV MESOS_VERSION 0.27.2  
ENV MESOS_PACKAGE_VERSION 2.0.15  
ENV MESOS_KAFKA_VERSION 0.9.5.0  
ENV KAFKA_VERSION 0.9.0.1  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF && \  
DISTRO=debian && \  
CODENAME=jessie && \  
echo "deb http://repos.mesosphere.io/${DISTRO} ${CODENAME} main" | tee
/etc/apt/sources.list.d/mesosphere.list && \  
echo "deb http://http.debian.net/${DISTRO} ${CODENAME}-backports main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install -yq --no-install-recommends \  
apt-utils \  
bash \  
curl \  
openjdk-${JAVA_VERSION}-jre-headless \  
mesos=${MESOS_VERSION}-${MESOS_PACKAGE_VERSION}.debian81 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /kafka-mesos  
WORKDIR /kafka-mesos  
RUN curl -O -k -L https://github.com/yagniio/docker-mesos-
kafka/releases/download/$MESOS_KAFKA_VERSION-$KAFKA_VERSION/kafka-
mesos-$MESOS_KAFKA_VERSION.jar  
RUN curl -O
http://archive.apache.org/dist/kafka/$KAFKA_VERSION/kafka_2.11-$KAFKA_VERSION.tgz  
ADD docker-entrypoint.sh /kafka-mesos/docker-entrypoint.sh  
  
ENTRYPOINT ["/kafka-mesos/docker-entrypoint.sh"]

