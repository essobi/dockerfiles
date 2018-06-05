# Copyright (C) 2015 Bitergia  
# GPLv3 License  
FROM centos:6  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV CYGNUS_USER "cygnus"  
ENV CYGNUS_HOME "/opt/fiware-cygnus"  
ENV GIT_URL_CYGNUS https://github.com/telefonicaid/fiware-cygnus.git  
ENV GIT_REV_CYGNUS release-0.8.2  
ENV MVN_VER "3.2.5"  
ENV MVN_TGZ "apache-maven-${MVN_VER}-bin.tar.gz"  
ENV MVN_URL
"http://www.eu.apache.org/dist/maven/maven-3/${MVN_VER}/binaries/${MVN_TGZ}"  
ENV MVN_HOME "/opt/apache-maven"  
ENV FLUME_VER "1.4.0"  
ENV FLUME_TGZ "apache-flume-${FLUME_VER}-bin.tar.gz"  
ENV FLUME_URL "http://archive.apache.org/dist/flume/${FLUME_VER}/${FLUME_TGZ}"  
ENV FLUME_HOME "/opt/apache-flume"  
ENV SUBSCRIPTIONS_PATH /opt/subscribe  
  
# Install java jdk 1.6.0, maven and flume  
ENV JAVA_HOME /usr/lib/jvm/java-1.6.0  
WORKDIR /opt  
  
RUN adduser --comment "${CYGNUS_USER}" ${CYGNUS_USER}  
  
RUN yum -y install tar nc which git java-1.6.0-openjdk-devel && \  
yum clean all && \  
curl --remote-name --location --insecure --silent --show-error "${MVN_URL}" &&
\  
tar xzvf ${MVN_TGZ} && \  
mv apache-maven-${MVN_VER} ${MVN_HOME} && \  
curl --remote-name --location --insecure --silent --show-error "${FLUME_URL}"
&& \  
tar zxf ${FLUME_TGZ} && \  
mv apache-flume-${FLUME_VER}-bin ${FLUME_HOME} && \  
mkdir -p ${FLUME_HOME}/plugins.d/cygnus && \  
mkdir -p ${FLUME_HOME}/plugins.d/cygnus/lib && \  
mkdir -p ${FLUME_HOME}/plugins.d/cygnus/libext && \  
chown -R root:root ${FLUME_HOME} && \  
# Install cygnus  
# make a shallow clone to help reduce final image size  
git clone --depth 1 ${GIT_URL_CYGNUS} ${CYGNUS_HOME} && \  
cd ${CYGNUS_HOME} && \  
git checkout ${GIT_REV_CYGNUS} && \  
${MVN_HOME}/bin/mvn clean compile exec:exec assembly:single && \  
cp target/cygnus-*-jar-with-dependencies.jar
${FLUME_HOME}/plugins.d/cygnus/lib/ && \  
cp target/classes/cygnus-flume-ng ${FLUME_HOME}/bin/ && \  
curl --remote-name --location --insecure --silent --show-error
http://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.9.1/libthrift-0.9.1.jar
&& \  
mv libthrift-0.9.1.jar ${FLUME_HOME}/lib/libthrift-0.7.0.jar && \  
chmod +x ${FLUME_HOME}/bin/cygnus-flume-ng && \  
mkdir /config && \  
mkdir ${SUBSCRIPTIONS_PATH} && \  
touch /subscribe-to-orion && \  
# Cleanup to thin the final image  
${MVN_HOME}/bin/mvn clean && \  
rm -rf /root/.m2 && \  
bash -c 'find /usr/share/locale -maxdepth 1 -mindepth 1 -type d | grep -v -e
"en_US" | xargs rm -rfv' && \  
bash -c 'localedef --list-archive | grep -v -e "en_US" | xargs localedef
--delete-from-archive' && \  
mv -f /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl && \  
build-locale-archive && \  
rm -f /opt/${MVN_TGZ} && \  
rm -f /opt/${FLUME_TGZ}  
  
COPY subscription-therm-sensors.sh ${SUBSCRIPTIONS_PATH}/  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
### Exposed ports  
# - Cygnus notifications are received on this port  
EXPOSE 5050  

