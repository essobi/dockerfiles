  
FROM java:openjdk-7-jdk  
# originally based on UNB Libraries Dockerfile  
MAINTAINER Andrew Jackson "anj@anjackson.net"  
  
# update packages and install maven  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y tar wget curl git maven  
  
  
  
# Prepare environment  
# ENV JAVA_HOME /opt/java  
#ENV CATALINA_HOME /opt/tomcat  
#ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin:$CATALINA_HOME/scripts  
  
# Install Oracle Java8  
#ENV JAVA_VERSION 8u131  
#ENV JAVA_BUILD 8u121-b11  
#ENV JAVA_DL_HASH d54c1d3a095b4ff2b6607d096fa80163  
  
#RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
# http://download.oracle.com/otn-
pub/java/jdk/${JAVA_BUILD}/${JAVA_DL_HASH}/jdk-${JAVA_VERSION}-linux-x64.tar.gz
&& \  
# tar -xvf jdk-${JAVA_VERSION}-linux-x64.tar.gz && \  
# rm jdk*.tar.gz && \  
# mv jdk* ${JAVA_HOME}  
  
# Java Version  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=144 \  
JAVA_BUILD=01 \  
JAVA_TOKEN=090f390dda5b47b9b721c7dfaa008135 \  
JAVA_HOME=/usr/lib/jvm/current-java  
  
# JDK: http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.tar.gz  
# JRE: http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jre-8u60-linux-x64.tar.gz  
# http://download.oracle.com/otn-
pub/java/jdk/8u101-b13/jdk-8u101-linux-x64.tar.gz  
# http://download.oracle.com/otn-
pub/java/jdk/8u111-b14/jdk-8u111-linux-x64.tar.gz  
# http://download.oracle.com/otn-
pub/java/jdk/8u121-b13/e9e7ea248e2c4826b92b3f075a80e441/jdk-8u121-linux-x64.tar.gz  
# http://download.oracle.com/otn-
pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/jre-8u141-linux-x64.tar.gz  
  
# JRE  
#RUN cd /tmp && wget --header "Cookie: oraclelicense=accept-securebackup-
cookie;" \  
# "http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_TOKEN}/jre-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"
&& \  
# tar xzf "jre-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \  
# mkdir -p /usr/lib/jvm && mv "/tmp/jre1.${JAVA_VERSION}.0_${JAVA_UPDATE}"
"/usr/lib/jvm/java-${JAVA_VERSION}-oracle" && \  
# ln -s "java-${JAVA_VERSION}-oracle" $JAVA_HOME && \  
# ln -s $JAVA_HOME/bin/java /usr/bin/java && \  
# rm -rf $JAVA_HOME/*.txt && \  
# rm -rf $JAVA_HOME/*.html && \  
# apk del wget ca-certificates curl && \  
# rm /tmp/* /var/cache/apk/*  
  
# JDK  
RUN cd /tmp && wget --header "Cookie: oraclelicense=accept-securebackup-
cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"
&& \  
tar xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" && \  
mkdir -p /usr/lib/jvm && mv "/tmp/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}"
"/usr/lib/jvm/java-${JAVA_VERSION}-oracle" && \  
ln -s "java-${JAVA_VERSION}-oracle" $JAVA_HOME && \  
ln -s $JAVA_HOME/bin/java /usr/bin/java && \  
rm -rf $JAVA_HOME/*.txt && \  
rm -rf $JAVA_HOME/*.html && \  
apk del wget ca-certificates curl && \  
rm /tmp/* /var/cache/apk/*  
  
  
  
  
# Install Tomcat  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.5.15  
  
RUN wget
http://ftp.riken.jp/net/apache/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz && \  
tar -xvf apache-tomcat-${TOMCAT_VERSION}.tar.gz && \  
rm apache-tomcat*.tar.gz && \  
mv apache-tomcat* ${CATALINA_HOME}  
  
RUN chmod +x ${CATALINA_HOME}/bin/*sh  
  
  
  
  
  
# move to /opt and download the tomcat package  
#RUN cd /opt && wget -q
"http://www.mirrorservice.org/sites/ftp.apache.org/tomcat/tomcat-7/v7.0.79/bin/apache-
tomcat-7.0.79.tar.gz" && \  
# cd /opt && tar -zxvf apache-tomcat-7.0.79.tar.gz && \  
# cd /opt && ln -sf apache-tomcat-7.0.79 tomcat  
  
# make tomcat scripts executable  
#RUN chmod +x /opt/tomcat/bin/*.sh  
  
# Cleanup webapps directory  
RUN cd /opt/tomcat/webapps && rm -rf *  
  
# Tweak Tomcat configuration  
COPY docker/server.xml /opt/tomcat/conf/server.xml  
COPY docker/logging.properties /opt/tomcat/conf/logging.properties  
  
# Install ICU4J in the system JVM for broader language support  
RUN \  
curl -O http://download.icu-project.org/files/icu4j/58.2/icu4j-58_2.jar && \  
curl -O http://download.icu-
project.org/files/icu4j/58.2/icu4j-localespi-58_2.jar && \  
mv icu4j-* /usr/lib/jvm/java-7-openjdk-amd64/jre/lib/ext/  
  
# Build UKWA Wayback versions inside the container...  
# Need a patched OpenWayback instance:  
RUN \  
git clone https://github.com/ukwa/openwayback.git && \  
cd openwayback && \  
git checkout restore-locale-switch && \  
mvn install -DskipTests  
  
# Now build our overlays:  
COPY . /waybacks  
RUN \  
cd waybacks && \  
mvn install -DskipTests  
  
# Define runtime properties  
  
EXPOSE 8080 8090  
  
ENV JAVA_OPTS -Xmx1g  
  
# Use oukwa|ldukwa|qa for Open UKWA, LD UKWA or QA UKWA versions  
ENV UKWA_OWB_VERSION=qa  
  
VOLUME /data  
  
#Fire up tomcat, copying desired WAR into place first  
COPY docker/start.sh /  
  
CMD /start.sh  
  
  

