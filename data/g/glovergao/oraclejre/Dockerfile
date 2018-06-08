FROM glovergao/javabase:latest  
MAINTAINER glover.gao@grapecity.com  
  
# Install Oracle JDK 7u80  
RUN cd /tmp \  
RUN curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k
"http://cms.ixiasoft.com/downloads/util/java/jre-7u80-linux-x64.gz" \  
RUN tar xf jre-7u80-linux-x64.gz -C ${JAVA_BASE} \  
RUN rm -f jre-7u80-linux-x64.gz \  
RUN ln -s ${JAVA_BASE}/jre* ${JAVA_BASE}/jre \  
RUN ln -s ${JAVA_BASE}/jre ${JAVA_BASE}/jvm \  
RUN rm -rf /var/lib/apt/lists/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
/var/cache/*  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME ${JAVA_BASE}/jre  
  
# Add /opt/java and jdk on PATH variable  
ENV PATH ${PATH}:${JAVA_HOME}/bin:${JAVA_BASE}

