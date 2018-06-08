FROM livingobjects/debian-base:9.2  
ENV JAVA_VERSION=8u152 \  
JAVA_BUILD_VERSION=8u152-b16  
  
# Install Java 8  
RUN wget -qO- --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_BUILD_VERSION}/aa0333dd3019491ca4f6ddbe78cdb6d0/jre-${JAVA_VERSION}-linux-x64.tar.gz
\  
| tar -xzf - -C /opt && \  
  
# Link default java to actual java version  
ln -s $(find /opt -name jre*) /opt/java && \  
ln -s /opt/java/bin/java /usr/bin/java && \  
ln -s /opt/java/bin/javac /usr/bin/javac && \  
  
# Clean installation form unused librairies  
rm -rf /opt/java/lib/plugin.jar \  
/opt/java/lib/ext/jfxrt.jar \  
/opt/java/bin/javaws \  
/opt/java/lib/javaws.jar \  
/opt/java/lib/desktop \  
/opt/java/plugin \  
/opt/java/lib/deploy* \  
/opt/java/lib/*javafx* \  
/opt/java/lib/*jfx* \  
/opt/java/lib/amd64/libdecora_sse.so \  
/opt/java/lib/amd64/libprism_*.so \  
/opt/java/lib/amd64/libfxplugins.so \  
/opt/java/lib/amd64/libglass.so \  
/opt/java/lib/amd64/libgstreamer-lite.so \  
/opt/java/lib/amd64/libjavafx*.so \  
/opt/java/lib/amd64/libjfx*.so && \  
# Set JAVA ENV vars  
echo "export JAVA_HOME=/opt/java" >> /etc/profile && \  
echo "export PATH=$PATH:/opt/java/bin" >> /etc/profile  

