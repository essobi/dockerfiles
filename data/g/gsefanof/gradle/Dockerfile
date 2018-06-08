FROM gradle:latest  
MAINTAINER gsefanof@gmail.com  
  
ENV JDK_URL http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz  
  
ENV JDK_HOME /usr/java/jdk  
ENV JAVA_HOME /usr/java/jre  
  
USER root  
  
RUN curl --silent --location --retry 3 http://pki.intelions.ru/private/ca.crt
-o /usr/local/share/ca-certificates/ca.intelions.ru.crt && \  
curl --silent --location --retry 3
http://pki.intelions.ru/private/ca_class1.crt -o /usr/local/share/ca-
certificates/ca_class1.intelions.ru.crt && \  
update-ca-certificates  
  
RUN mkdir -p ${JDK_HOME} && ln -s ${JDK_HOME}/jre $JAVA_HOME && \  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" "$JDK_URL" \  
| tar -xz --strip-components=1 -C ${JDK_HOME}  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws"  
  
RUN rm -f "${JAVA_HOME}/lib/security/cacerts" && \  
ln -s /etc/ssl/certs/java/cacerts "${JAVA_HOME}/lib/security/cacerts"  
  
USER gradle  

