FROM isuper/base-ubuntu  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
MAINTAINER John Dondapati <john@apex-its.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV VERSION 8  
ENV UPDATE 74  
ENV BUILD 02  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
ENV JRE_HOME ${JAVA_HOME}/jre  
  
ENV OPENSSL_VERSION 1.0.2f  
  
RUN apt-get update && apt-get install ca-certificates curl \  
gcc libc6-dev libssl-dev make \  
-y --no-install-recommends && \  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/server-
jre-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz \  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GlobalSign_Root_CA.pem \  
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \  
| tar xz -C /tmp && \  
cd /tmp/openssl-${OPENSSL_VERSION} && \  
./config --prefix=/usr && \  
make clean && make && make install && \  
apt-get remove --purge --auto-remove -y \  
gcc \  
libc6-dev \  
libssl-dev \  
make && \  
apt-get autoclean && apt-get --purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JRE_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --set java "${JRE_HOME}/bin/java" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac"  
  
ENV CATALINA_HOME /opt/tomcat  
ENV PATH $CATALINA_HOME/bin:$PATH  
RUN mkdir -p "$CATALINA_HOME"  
WORKDIR $CATALINA_HOME  
  
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
  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.32  
ENV TOMCAT_TGZ_URL
https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz*  
  
#Patching the tomcat to create a admin user.  
RUN cp $CATALINA_HOME/conf/tomcat-users.xml $CATALINA_HOME/conf/tomcat-
users.org.xml  
RUN sed 's?.*/tomcat-users>.*?<role rolename="manager-gui"/>\n <role
rolename="admin-gui"/> \n <user username="admin" password="admin"
roles="admin-gui, manager-gui"/> \n\n&?' $CATALINA_HOME/conf/tomcat-users.xml
> $CATALINA_HOME/conf/tomcat-users.new.xml  
RUN mv $CATALINA_HOME/conf/tomcat-users.new.xml $CATALINA_HOME/conf/tomcat-
users.xml  
  
WORKDIR $CATALINA_HOME/bin  
  
EXPOSE 8080 8443 80 443  
CMD ["/opt/tomcat/bin/catalina.sh", "run"]  

