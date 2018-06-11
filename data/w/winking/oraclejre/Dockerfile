FROM winking/javabase:latest  
MAINTAINER winking.zhang@grapecity.com  
  
# Install Oracle JDK 7u80  
RUN cd /tmp && \  
curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k
"http://download.oracle.com/otn-
pub/java/jdk/7u80-b15/jre-7u80-linux-x64.tar.gz" && \  
tar xf jre-7u80-linux-x64.tar.gz -C ${JAVA_BASE} && \  
rm -f jre-7u80-linux-x64.tar.gz && \  
ln -s ${JAVA_BASE}/jre* ${JAVA_BASE}/jre && \  
ln -s ${JAVA_BASE}/jre ${JAVA_BASE}/jvm && \  
rm -rf /var/lib/apt/lists/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/*  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME ${JAVA_BASE}/jre  
  
# Add /opt/java and jdk on PATH variable  
ENV PATH ${PATH}:${JAVA_HOME}/bin:${JAVA_BASE}  

