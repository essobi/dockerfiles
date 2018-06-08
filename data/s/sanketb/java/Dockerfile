FROM progrium/busybox  
MAINTAINER Sanket Bajoria <bajoriasanket@gmail.com>  
# Based on https://github.com/develar/docker-java  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=45 \  
JAVA_VERSION_BUILD=14 \  
JAVA_PACKAGE=server-jre \  
JAVA_HOME=/jre \  
PATH=${PATH}:/jre/bin \  
LANG=C.UTF-8  
RUN opkg-install curl ca-certificates && \  
cd /tmp && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
| gunzip -c - | tar -xf - && \  
mv jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}/jre /jre && \  
opkg-cl remove ca-certificates && \  
# rm -rf /tmp/* && \  
echo 'networkaddress.cache.ttl = 60' >> /jre/lib/security/java.security  
  
CMD ["sh"]  

