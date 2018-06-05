FROM oraclelinux:6  
MAINTAINER Trevor Fuson "trevor.fuson@unbc.ca"  
RUN rpm --rebuilddb \  
&& yum -y install tar \  
vim \  
patch \  
gcc \  
openssl-devel \  
apr-devel \  
&& yum clean all  
  
# Java Download location. Note the build number is in the URL.  
#
http://www.oracle.com/technetwork/java/javase/downloads/jdk7-downloads-1880260.html  
ENV JAVA_MINOR_VERSION 79  
ENV JAVA_BUILD_NUMBER 15  
ENV JAVA_HOME /usr/java/jdk1.7.0_$JAVA_MINOR_VERSION  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Install Java JDK without leaving behind temporary files  
RUN curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/7u$JAVA_MINOR_VERSION-b$JAVA_BUILD_NUMBER/jdk-7u$JAVA_MINOR_VERSION-
linux-x64.rpm > jdk-7u$JAVA_MINOR_VERSION-linux-x64.rpm && \  
rpm -ivh jdk-7u$JAVA_MINOR_VERSION-linux-x64.rpm && \  
rm jdk-7u$JAVA_MINOR_VERSION-linux-x64.rpm  
  
ENV CATALINA_HOME /usr/local/tomcat  
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
713DA88BE50911535FE716F5208B0AB1D63011C7 \  
79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \  
9BA44C2621385CB966EBA586F72C284D731FABEE \  
A27677289986DB50844682F8ACB77FC2E86E29AC \  
A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \  
DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \  
F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \  
F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23  
  
ENV TOMCAT_MAJOR 7  
ENV TOMCAT_VERSION 7.0.61  
ENV TOMCAT_TGZ_URL
https://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \  
&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \  
&& gpg --verify tomcat.tar.gz.asc \  
&& tar -xvf tomcat.tar.gz --strip-components=1 \  
&& rm bin/*.bat \  
&& rm tomcat.tar.gz* \  
&& rm -rf $CATALINA_HOME/webapps/*  
  
#Install the tomcat native libraries for improved SSL performance  
ENV TOMCAT_NATIVE_VERSION=1.1.33  
ENV TOMCAT_NATIVE_URL=http://archive.apache.org/dist/tomcat/tomcat-
connectors/native/$TOMCAT_NATIVE_VERSION/source/tomcat-
native-$TOMCAT_NATIVE_VERSION-src.tar.gz  
  
RUN set -x \  
&& curl -fSL "$TOMCAT_NATIVE_URL" -o tomcat-native-$TOMCAT_NATIVE_VERSION-
src.tar.gz \  
&& curl -fSL "$TOMCAT_NATIVE_URL.sha1" -o tomcat-
native-$TOMCAT_NATIVE_VERSION-src.tar.gz.sha1 \  
&& sha1sum -c tomcat-native-$TOMCAT_NATIVE_VERSION-src.tar.gz.sha1 \  
&& mkdir tomcat-native \  
&& tar -xvf tomcat-native-$TOMCAT_NATIVE_VERSION-src.tar.gz --strip-
components=1 -C tomcat-native \  
&& cd tomcat-native/jni/native \  
&& ./configure --with-apr=/usr/bin/apr-1-config \  
&& make \  
&& make install \  
&& ln -s /usr/local/apr/lib/libtcnative-1.so /usr/lib/libtcnative-1.so \  
&& cd $CATALINA_HOME \  
&& rm -rf tomcat-native-$TOMCAT_NATIVE_VERSION-src.tar.gz* \  
&& rm -rf tomcat-native  
  
#Patch the server configuration to turn on SSL for port 8443, and patch
catalina.sh so that it generates and uses a new self signed cert on each run.  
COPY serverxmlpatch $CATALINA_HOME/  
COPY catalinapatch $CATALINA_HOME/  
RUN patch $CATALINA_HOME/conf/server.xml $CATALINA_HOME/serverxmlpatch ;\  
patch $CATALINA_HOME/bin/catalina.sh $CATALINA_HOME/catalinapatch  
  
EXPOSE 8443  
CMD ["catalina.sh", "run"]

