FROM debian:jessie  
MAINTAINER Krzysztof Kardasz <krzysztof@kardasz.eu>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y dist-upgrade && \  
apt-get -y install wget curl ca-certificates libav-tools libavcodec-extra
mediainfo libimage-exiftool-perl  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# Download Oracle JDK  
ENV ORACLE_JDK_VERSION jdk-8u92  
ENV ORACLE_JDK_URL http://download.oracle.com/otn-
pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.tar.gz  
RUN mkdir -p /opt/jdk/$ORACLE_JDK_VERSION && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" -O
/opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz $ORACLE_JDK_URL && \  
tar -zxf /opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz --strip-
components=1 -C /opt/jdk/$ORACLE_JDK_VERSION && \  
chown -R root:root /opt/jdk/$ORACLE_JDK_VERSION && \  
rm /opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz && \  
update-alternatives --install /usr/bin/java java
/opt/jdk/$ORACLE_JDK_VERSION/bin/java 100 && \  
update-alternatives --install /usr/bin/javac javac
/opt/jdk/$ORACLE_JDK_VERSION/bin/javac 100  
  
ENV JAVA_HOME /opt/jdk/$ORACLE_JDK_VERSION  
ENV JAVA_VERSION 8u92  
ENV JAVA_TRUSTSTORE ${JAVA_HOME}/jre/lib/security/cacerts  
ENV JAVA_TRUSTSTORE_PASSWORD changeit  
ENV JAVA_OPTS "-Djavax.net.ssl.trustStore=${JAVA_TRUSTSTORE}
-Djavax.net.ssl.trustStorePassword=${JAVA_TRUSTSTORE_PASSWORD}"  
# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \  
05AB33110949707C93A279E3D3EFE6B686867BA6 \  
07E48665A34DCAFAE522E5E6266191C37C037D42 \  
47309207D818FFD8DCD3F83F1931D684307A10A5 \  
541FBE7D8F78B25E055DDEE13C370389288584E7 \  
61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER tomcat  
ENV RUN_USER_UID 5888  
ENV RUN_GROUP tomcat  
ENV RUN_GROUP_GID 5888  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.35  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
ENV CATALINA_HOME /usr/local/tomcat  
  
ENV PATH $CATALINA_HOME/bin:$JAVA_HOME/bin:$PATH  
  
RUN mkdir -p "$CATALINA_HOME"  
  
WORKDIR $CATALINA_HOME  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
RUN mkdir -p ${CATALINA_HOME}/webapp  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8080  
CMD ["catalina.sh", "run"]  

