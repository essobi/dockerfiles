FROM java:8-jdk  
MAINTAINER Alan Schegrer <flyinprogrammer@gmail.com>  
  
ENV ZK_VERSION=3.4.6 \  
EXHIBITOR_BRANCH=master \  
EXHIBITOR_VERSION=1.5.6 \  
PATH=${PATH}:/opt/zk/bin:/opt/mvn/bin  
  
RUN mkdir -p /opt/zk /opt/zk/transactions /opt/zk/snapshots && \  
curl -Lo /tmp/zk.tar.gz \  
http://www.apache.org/dist/zookeeper/zookeeper-${ZK_VERSION}/zookeeper-${ZK_VERSION}.tar.gz
&& \  
tar -xzf /tmp/zk.tar.gz -C /opt/zk --strip=1 && \  
rm -rf /tmp/*  
  
RUN apt-get update && \  
apt-get install -y git && \  
mkdir -p /opt/src && \  
cd /opt/src && \  
git clone \--depth 1 https://github.com/flyinprogrammer/exhibitor.git && \  
cd exhibitor && \  
git checkout ${EXHIBITOR_BRANCH} && \  
./gradlew -Prelease.version=${EXHIBITOR_VERSION} install && \  
cd exhibitor-standalone/src/main/resources/buildscripts/standalone/gradle/ &&
\  
../../../../../../../gradlew shadowJar && \  
mkdir -p /opt/exhibitor && \  
mv build/libs/exhibitor-${EXHIBITOR_VERSION}-all.jar
/opt/exhibitor/exhibitor.jar && \  
apt-get purge -y git && \  
apt-get autoremove -y && \  
apt-get clean autoclean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ \  
/opt/src \  
$HOME/.gradle \  
$HOME/.m2  
  
ENV CP_VERSION=2.4.3 \  
CP_SHA1=2c469a0e79a7ac801f1c032c2515dd0278134790  
  
RUN set -x && \  
curl -fSL
"https://github.com/joyent/containerpilot/releases/download/${CP_VERSION}/containerpilot-${CP_VERSION}.tar.gz"
-o cp.tar.gz && \  
echo "${CP_SHA1} ./cp.tar.gz" | sha1sum -c - && \  
tar -xzvf cp.tar.gz && \  
mv ./containerpilot /bin/ && \  
chmod +x /bin/containerpilot && \  
rm cp.tar.gz && \  
containerpilot -version  
  
COPY wrapper.sh /opt/exhibitor/wrapper.sh  
COPY zk.log4j.properties /opt/zk/conf/log4j.properties  
COPY app.json /opt/exhibitor/app.json  
ENV CONTAINERPILOT=file:///opt/exhibitor/app.json  
  
USER root  
WORKDIR /opt/exhibitor  
EXPOSE 2181 2888 3888 8181  
CMD ["containerpilot", "/opt/exhibitor/wrapper.sh"]

