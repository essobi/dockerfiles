# Java docker container  
# source: http://heiber.im/post/creating-a-solid-docker-base-image/  
#  
# build: docker build -t exoplatform/jmxtrans:latest .  
FROM openjdk:8-jdk  
LABEL maintainer="eXo Platform <docker@exoplatform.com>"  
  
ARG JMXTRANS_VERSION=268  
ENV TINI_VERSION v0.14.0  
ENV GOSU_VERSION 1.10  
ENV TERM=xterm \  
# Local  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
# JMXTrans  
JMXTRANS_APP_DIR=/opt/jmxtrans \  
JMXTRANS_JAR_FILE=jmxtrans-all.jar \  
JMXTRANS_JSON_DIR=/etc/jmxtrans \  
LOG_DIR=/var/log/jmxtrans \  
PATH=${PATH}:/opt  
  
WORKDIR /tmp  
  
# Installing Tini  
RUN set -ex \  
&& ( \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
|| gpg --keyserver pgp.mit.edu --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
|| gpg --keyserver keyserver.pgp.com --recv-keys
595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \  
)  
  
RUN set -ex \  
&& wget -O /usr/local/bin/tini
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini \  
&& wget -O /usr/local/bin/tini.asc
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc \  
&& gpg --verify /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini  
  
# Installing Gosu  
RUN set -ex \  
&& ( \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
|| gpg --keyserver pgp.mit.edu --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
|| gpg --keyserver keyserver.pgp.com --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
)  
  
RUN set -ex \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Installing JMXTrans  
RUN set -eux \  
echo "Downloading
http://central.maven.org/maven2/org/jmxtrans/jmxtrans/${JMXTRANS_VERSION}/jmxtrans-${JMXTRANS_VERSION}-all.jar"
\  
&& mkdir -p "${JMXTRANS_APP_DIR}" \  
&& curl -Lo "${JMXTRANS_APP_DIR}/${JMXTRANS_JAR_FILE}"
"http://central.maven.org/maven2/org/jmxtrans/jmxtrans/${JMXTRANS_VERSION}/jmxtrans-${JMXTRANS_VERSION}-all.jar"
\  
&& mkdir -p ${LOG_DIR} \  
&& rm -rf /tmp/*  
  
COPY jmxtrans.sh ${JMXTRANS_APP_DIR}/jmxtrans.sh  
COPY log4j.xml ${JMXTRANS_APP_DIR}/log4j.xml  
COPY conf/ ${JMXTRANS_JSON_DIR}  
  
RUN chmod +x ${JMXTRANS_APP_DIR}/jmxtrans.sh  
  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
CMD ["/opt/jmxtrans/jmxtrans.sh", "start", "/etc/jmxtrans"]

