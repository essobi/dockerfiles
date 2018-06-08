FROM ubuntu:14.04  
MAINTAINER Elium Tech <tech@elium.io>  
  
#### Some args to build the docker --build-args  
ENV SSL_STOREPASS=changeit  
ENV SSL_KEYPASS=changeit  
ENV SSL_DOMAIN_NAME="elium.io"  
#### set environment to fix term not set issues when building docker image
####  
ENV DEBIAN_FRONTEND noninteractive  
  
#### Set Nexus environment variables ####  
ENV SONATYPE_WORK /opt/nexus/  
ENV SSL_WORK /etc/ssl/private  
ENV NEXUS_DATA /nexus-data  
ENV NEXUS_VERSION 3.0.0-03  
#### Add run script ####  
ADD run ${SONATYPE_WORK}/bin/run  
RUN chmod +x ${SONATYPE_WORK}/bin/run  
  
#### Add packages to source list ####  
RUN \  
apt-get -y update && \  
# Make sure the package repository is up to date.  
apt-get install -y software-properties-common && \  
echo 'deb http://downloads.sourceforge.net/project/ubuntuzilla/mozilla/apt all
main' > /etc/apt/sources.list.d/ubuntuzilla.list && \  
apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C1289A29 && \  
# oracle java 8  
add-apt-repository -y ppa:webupd8team/java  
  
#### run update ####  
RUN apt-get -y update  
  
#### install tools ####  
RUN apt-get install -y curl tar gzip apt-transport-https ca-certificates
libsystemd-journal0 sudo && \  
apt-get autoremove && \  
apt-get clean all  
  
#### install oracle java 8 ####  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
#### Define commonly used JAVA_HOME variable ####  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#### install nexus ####  
RUN mkdir -p ${SONATYPE_WORK} && \  
curl --fail --silent --location --retry 3
https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz \  
| gunzip \  
| tar x -C ${SONATYPE_WORK} \--strip-components=1 nexus-${NEXUS_VERSION} && \  
rm -rf /tmp/nexus* && \  
chown -R root:root ${SONATYPE_WORK}  
  
#### Enable SSL ####  
RUN mkdir -p ${SONATYPE_WORK}etc/ssl  
  
#### Configure Nexus for SSL ####  
RUN sed -i -e '/nexus-args=/
s/=.*/=${karaf.etc}\/jetty.xml,${karaf.etc}\/jetty-
requestlog.xml,${karaf.etc}\/jetty-http.xml,${karaf.etc}\/jetty-
https.xml,${karaf.etc}\/jetty-http-redirect-to-https.xml/'
${SONATYPE_WORK}etc/org.sonatype.nexus.cfg \  
&& echo "application-port-ssl=8443" >>
${SONATYPE_WORK}etc/org.sonatype.nexus.cfg \  
&& sed -i 's/<Set name="KeyStorePath">.*<\/Set>/<Set
name="KeyStorePath">\/opt\/nexus\/etc\/ssl\/server-keystore.jks<\/Set>/g'
/${SONATYPE_WORK}etc/jetty-https.xml \  
&& sed -i 's/<Set name="KeyStorePassword">.*<\/Set>/<Set
name="KeyStorePassword">changeit<\/Set>/g' ${SONATYPE_WORK}etc/jetty-https.xml
\  
&& sed -i 's/<Set name="KeyManagerPassword">.*<\/Set>/<Set
name="KeyManagerPassword">changeit<\/Set>/g' ${SONATYPE_WORK}etc/jetty-
https.xml \  
&& sed -i 's/<Set name="TrustStorePath">.*<\/Set>/<Set
name="TrustStorePath">\/opt\/nexus\/etc\/ssl\/server-keystore.jks<\/Set>/g'
${SONATYPE_WORK}etc/jetty-https.xml \  
&& sed -i 's/<Set name="TrustStorePassword">.*<\/Set>/<Set
name="TrustStorePassword">changeit<\/Set>/g' ${SONATYPE_WORK}etc/jetty-
https.xml  
  
#### Add User Nexus ####  
RUN useradd -r -u 200 -m -c "nexus role account" -d ${NEXUS_DATA} -s
/bin/false nexus && \  
chown -R nexus ${SONATYPE_WORK}  
  
#### configure nexus runtime env ####  
RUN sed \  
-e "s|karaf.home=.|karaf.home=${SONATYPE_WORK}|g" \  
-e "s|karaf.base=.|karaf.base=${SONATYPE_WORK}|g" \  
-e "s|karaf.etc=etc|karaf.etc=${SONATYPE_WORK}etc|g" \  
-e "s|java.util.logging.config.file=etc|java.util.logging.config.file=${SONATYPE_WORK}etc|g" \  
-e "s|karaf.data=data|karaf.data=${NEXUS_DATA}|g" \  
-e "s|java.io.tmpdir=data/tmp|java.io.tmpdir=${NEXUS_DATA}/tmp|g" \  
-i ${SONATYPE_WORK}bin/nexus.vmoptions  
  
VOLUME ${NEXUS_DATA}  
VOLUME ${SSL_WORK}  
  
#### http, https, https for docker group, https for hosted docker hub ####  
EXPOSE 8081 5000 5001  
#### USER nexus ####  
WORKDIR ${SONATYPE_WORK}  
  
ENV JAVA_MAX_MEM 1200m  
ENV JAVA_MIN_MEM 1200m  
ENV EXTRA_JAVA_OPTS ""  
CMD bin/run

