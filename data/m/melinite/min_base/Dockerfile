# oracle java 8 bb min base  
FROM melinite/min_base  
MAINTAINER David Seong <melinite@gmail.com>  
  
USER root  
  
ENV JAVA_VERSION_MAJOR=8 JAVA_VERSION_MINOR=31 JAVA_VERSION_BUILD=13
JAVA_PACKAGE=server-jre \  
JAVA_HOME=/opt/jdk  
  
  
RUN mkdir -p /opt && \  
curl -# -kLOH "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
gunzip
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
tar -xf
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar -C
/opt && \  
rm ${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar
&& \  
mv /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
  

