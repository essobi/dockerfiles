FROM orctom/alpine:3.2  
MAINTAINER Hao Chen <orctom@gmail.com>  
  
ENV JAVA_VERSION_MAJOR 7  
ENV JAVA_VERSION_MINOR 79  
ENV JAVA_VERSION_BUILD 15  
ENV PACKAGE_TYPE server-jre  
  
ENV JAVA_HOME /usr/lib/jvm/java-${JAVA_VERSION_MAJOR}-oracle  
  
RUN \  
apk add --update curl tar && rm -rf /var/cache/apk/* \  
&& mkdir -p $JAVA_HOME \  
&& curl -jkLH "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${PACKAGE_TYPE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
-o
/tmp/${PACKAGE_TYPE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
&& tar -xf
/tmp/${PACKAGE_TYPE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
-C $JAVA_HOME --strip-components=1 \  
&& rm
/tmp/${PACKAGE_TYPE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
&& ln -s $JAVA_HOME/bin/java /usr/bin/java \  
&& ln -s $JAVA_HOME/bin/javac /usr/bin/javac \  
&& rm -rf $JAVA_HOME/*src.zip \  
$JAVA_HOME/lib/missioncontrol \  
$JAVA_HOME/lib/visualvm \  
$JAVA_HOME/lib/*javafx* \  
$JAVA_HOME/jre/lib/ext/jfxrt.jar \  
$JAVA_HOME/jre/bin/javaws \  
$JAVA_HOME/jre/lib/javaws.jar \  
$JAVA_HOME/jre/lib/desktop \  
$JAVA_HOME/jre/lib/*javafx* \  
$JAVA_HOME/jre/lib/*jfx*  
  
ENV PATH $PATH:$JAVA_HOME/bin

