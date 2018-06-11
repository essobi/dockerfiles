FROM progrium/busybox  
  
MAINTAINER Whisk Tech <tech@whisk.com>  
  
RUN opkg-install curl ca-certificates bash  
  
ENV JAVA_HOME /usr/jdk1.8.0_45  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/GeoTrust_Global_CA.crt \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-pub/java/jdk/8u45-b14/server-
jre-8u45-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/*src.zip \  
$JAVA_HOME/man \  
$JAVA_HOME/lib/missioncontrol \  
$JAVA_HOME/lib/visualvm \  
$JAVA_HOME/lib/*javafx* \  
$JAVA_HOME/jre/lib/plugin.jar \  
$JAVA_HOME/jre/lib/ext/jfxrt.jar \  
$JAVA_HOME/jre/bin/javaws \  
$JAVA_HOME/jre/lib/javaws.jar \  
$JAVA_HOME/jre/lib/desktop \  
$JAVA_HOME/jre/plugin \  
$JAVA_HOME/jre/lib/deploy* \  
$JAVA_HOME/jre/lib/*javafx* \  
$JAVA_HOME/jre/lib/*jfx* \  
$JAVA_HOME/jre/lib/amd64/libdecora_sse.so \  
$JAVA_HOME/jre/lib/amd64/libprism_*.so \  
$JAVA_HOME/jre/lib/amd64/libfxplugins.so \  
$JAVA_HOME/jre/lib/amd64/libglass.so \  
$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so \  
$JAVA_HOME/jre/lib/amd64/libjavafx*.so \  
$JAVA_HOME/jre/lib/amd64/libjfx*.so  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin  

