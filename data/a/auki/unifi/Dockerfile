# FROM debian:stretch-slim  
FROM ubuntu:xenial  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
ENV PKGURL=https://dl.ubnt.com/unifi/5.7.23/unifi_sysvinit_all.deb  
  
RUN apt-get update && \  
apt-get install -qy --no-install-recommends \  
ca-certificates \  
openjdk-8-jre-headless \  
curl && \  
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4
multiverse" > /etc/apt/sources.list.d/mongodb-org.list && \  
echo "deb http://www.ubnt.com/downloads/unifi/debian stable unifi" >
/etc/apt/sources.list.d/unifi.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50 && \  
apt-get update && \  
curl -L -o ./unifi.deb "${PKGURL}" && \  
apt-get purge -qy --auto-remove \  
ca-certificates && \  
apt -qy install mongodb-org ./unifi.deb && \  
rm -f ./unifi.deb && \  
apt-get clean -qy && \  
rm -rf /var/lib/apt/lists/*  
  
ENV BASEDIR=/usr/lib/unifi \  
DATADIR=/var/lib/unifi \  
RUNDIR=/var/run/unifi \  
LOGDIR=/var/log/unifi \  
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \  
JVM_MAX_HEAP_SIZE=1024M \  
JVM_INIT_HEAP_SIZE=  
  
RUN ln -s ${LOGDIR} ${BASEDIR}/logs && \  
ln -s ${RUNDIR} ${BASEDIR}/run && \  
ln -s ${DATADIR} ${BASEDIR}/data  
  
VOLUME ["${DATADIR}", "${RUNDIR}", "${LOGDIR}"]  
  
EXPOSE 6789/tcp 8080/tcp 8443/tcp 8880/tcp 8843/tcp 3478/udp  
  
WORKDIR ${BASEDIR}  
  
COPY entrypoint.sh /entrypoint.sh  
COPY prune.sh /prune.sh  
COPY prune.js /prune.js  
RUN chmod +x /entrypoint.sh && chmod +x /prune.sh  
  
#HEALTHCHECK CMD curl -kILs --fail https://localhost:8443 || exit 1  
CMD ["/entrypoint.sh"]

