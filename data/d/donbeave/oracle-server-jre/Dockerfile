FROM buildpack-deps:wheezy-curl  
  
MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>  
  
LABEL version=8u92  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
  
ENV JAVA_MAJOR 8  
ENV JAVA_VERSION 8u92  
ENV JAVA_BUILD 8u92-b14  
ENV JAVA_FULL_VERSION 1.8.0_92  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JAVA_TGZ_URL http://download.oracle.com/otn-
pub/java/jdk/$JAVA_BUILD/server-jre-$JAVA_VERSION-linux-x64.tar.gz  
  
RUN set -x \  
&& wget --header "Cookie: oraclelicense=accept-securebackup-cookie"
$JAVA_TGZ_URL \  
&& mkdir -p /usr/lib/jvm \  
&& tar -xzvf server-jre-$JAVA_VERSION-linux-x64.tar.gz -C /usr/lib/jvm \  
&& rm server-jre-$JAVA_VERSION-linux-x64.tar.gz \  
&& mv /usr/lib/jvm/jdk$JAVA_FULL_VERSION $JAVA_HOME \  
&& chown --recursive root:root $JAVA_HOME \  
&& update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 100 \  
&& update-alternatives --display java \  
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 100
\  
&& update-alternatives --display javac  
  
ENV PATH $JAVA_HOME/bin:$PATH  
  
WORKDIR $JAVA_HOME  
  
# If you're reading this and have any feedback on how this image could be  
# improved, please open an issue or a pull request so we can discuss it!  

