FROM parana/centos7  
  
# Based on centos:7.2.1511 Public Image  
MAINTAINER "larry king" <jiangguoqing@stars.org.cn>`  
  
ENV REFRESHED_AT 2016-12-13  
#  
# If you prefer download file for yourself, please execute: cd install && curl
-O http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz to
Download binary files  
#  
# Set environment  
ENV JAVA_HOME /opt/jdk1.8.0_91  
ENV PATH ${JAVA_HOME}/bin:${PATH}:.  
  
# Java Version 1.8.0_91-b14  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 91  
ENV JAVA_VERSION_BUILD 14  
ENV JAVA_PACKAGE jdk  
ENV ORACLE_SITE download.oracle.com/otn-pub/java/jdk  
ENV JAVA_FILE
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz  
  
ENV JAVA_OPTS="-Xms512m -Xmx1024m"  
# install net-tools & vim  
RUN yum -y install net-tools && \  
yum -y install vim  
  
COPY install /tmp/  
# RUN find /tmp -type d | sort  
# File was splited using: split -b 240000k ../spark-2.0.1-bin-hadoop2.7.tgz  
WORKDIR /tmp  
  
RUN echo "Generating spark-2.0.1-bin-hadoop2.7.tgz file" && \  
cd spark-2.0.1-bin-hadoop2.7 && \  
cat x* > spark-2.0.1-bin-hadoop2.7.tar.gz && \  
rm -rf x* && \  
tar -xzf spark-2.0.1-bin-hadoop2.7.tar.gz && \  
rm -rf spark-2.0.1-bin-hadoop2.7.tar.gz && \  
mv spark-2.0.1-bin-hadoop2.7 /usr/local/spark && \  
cd .. && rm -rf spark-2.0.1-bin-hadoop2.7 && \  
chown root:root -R /usr/local/spark  
  
# add spark application start scripts  
ENV PATH ${JAVA_HOME}/bin:/usr/local/spark/sbin:/usr/local/spark/bin:${PATH}:.  
  
# Ports  
EXPOSE 4040 6066 7077 8080 8081  
RUN echo "Generating ${JAVA_FILE}" && \  
cd jdk8 && cat xaa xab xac xad > ${JAVA_FILE} && \  
rm -rf xaa xab xac xad  
  
# unarchive Java  
RUN cd jdk8 && \  
cat ${JAVA_FILE} | tar -xzf - -C /opt && \  
chown root:root -R /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} &&
\  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so  
  
ENV TINI_VERSION 0.9.0  
# RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest |
grep -o "/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
# echo "TINI_VERSION = ${TINI_VERSION}"  
RUN ls -lat tini-rpm && \  
cd tini-rpm && \  
yum install -y tini_${TINI_VERSION}.rpm && \  
cd .. && \  
rm -rf tini-rpm && \  
yum clean all  
  
RUN cd maven3 && \  
tar xzf apache-maven-3.3.9-bin.tar.gz && \  
chown root:root -R apache-maven-3.3.9 && \  
mv apache-maven-3.3.9 /usr/local/maven3 && \  
rm -rf apache-maven-3.3.9-bin.tar.gz  
  
ENV PATH /usr/local/maven3/bin:${PATH}  
  
RUN mkdir -p /desenv/java && mvn -v  
  
COPY test /desenv/java/  
  
WORKDIR /desenv/java  
  
# VOLUME /root/.m2/repository  
COPY m2-repo /root/.m2/repository  
# test requires large memory configured on JVM  
# RUN cd myspark && mvn clean compile test package install  
RUN cd myspark && mvn clean compile package install -Dmaven.test.skip=true  
  
# add hive conf  
COPY hive-site.xml /usr/local/spark/conf/hive-site.xml  
  
# copy depoly script  
RUN mkdir /start_script  
COPY depoly_metastore.sh /start_script/depoly_metastore.sh  
RUN chmod a+x /start_script/depoly_metastore.sh  
WORKDIR /start_script  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
  
CMD [ "/bin/bash" ]  

