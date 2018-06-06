FROM cloutainer/k8s-jenkins-slave-base:v21  
  
#  
# USER: super  
#  
USER root  
  
#  
# ATLASSIAN SDK  
#  
ENV ATLS_VERSIN 6.3.10  
ENV ATLS_SHA512
c4be1f24d1e54757173fbc72400e72bb3e07942b628a666c4460c767c70090e391a23101e19d95776314778600961d09a1374b9193eefc139c0aa269da2345b5  
RUN echo "${ATLS_SHA512} /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz" >
/opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz.sha512 && \  
curl -jkSL -o /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz \  
https://maven.atlassian.com/content/repositories/atlassian-
public/com/atlassian/amps/atlassian-plugin-sdk/${ATLS_VERSIN}/atlassian-
plugin-sdk-${ATLS_VERSIN}.tar.gz && \  
sha512sum /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz && \  
sha512sum -c /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz.sha512 && \  
tar -C /opt -xf /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz && \  
chown -R jenkins:root /opt/atlassian-plugin-sdk-${ATLS_VERSIN} && \  
rm -f /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz  
  
#  
# ORACLE JAVA  
#  
ENV JAVA_VMAJOR 8  
ENV JAVA_VMINOR 161  
ENV JAVA_SHA512
09b58bd26e45e9eb84347977c0ea1b7d626fbfcc3f5ae717b25234156bdde0cdd35c81db674f0fa5351466cee206e48740997d08c7c33c2f78e5a043a485ab16  
ENV JAVA_DOHASH 2f38c3b165be4555a1fa6e98c45e0808  
RUN echo "${JAVA_SHA512}
/opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz" >
/opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz.sha512 && \  
curl -jkSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VMAJOR}u${JAVA_VMINOR}-b12/${JAVA_DOHASH}/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz
&& \  
sha512sum /opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz && \  
sha512sum -c /opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz.sha512 &&
\  
tar -C /opt -xf /opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz && \  
mv /opt/jdk1.${JAVA_VMAJOR}.0_${JAVA_VMINOR} /opt/jdk && \  
rm -f /opt/jdk-${JAVA_VMAJOR}u${JAVA_VMINOR}-linux-x64.tar.gz && \  
rm -f /opt/jdk/src.zip /opt/jdk/javafx-src.zip && \  
chown jenkins /opt/jdk/jre/lib/security/cacerts && \  
update-alternatives --install "/usr/bin/java" "java" "/opt/jdk/bin/java" 1 &&
\  
update-alternatives --install "/usr/bin/javac" "javac" "/opt/jdk/bin/javac" 1
&& \  
update-alternatives --install "/usr/bin/javaws" "javaws" "/opt/jdk/bin/javaws"
1 && \  
update-alternatives --install "/usr/bin/jar" "jar" "/opt/jdk/bin/jar" 1 && \  
update-alternatives --set "java" "/opt/jdk/bin/java" && \  
update-alternatives --set "javac" "/opt/jdk/bin/javac" && \  
update-alternatives --set "javaws" "/opt/jdk/bin/javaws" && \  
update-alternatives --set "jar" "/opt/jdk/bin/jar"  
#  
# APACHE MAVEN  
#  
RUN curl -jkSL -o /opt/maven.tar.gz
http://ftp.fau.de/apache/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz && \  
tar -C /opt -xf /opt/maven.tar.gz && \  
rm -f /opt/maven.tar.gz && \  
mv /opt/apache-maven-* /opt/apache-maven/  
  
#  
# GRADLE  
#  
RUN curl -jkSL -o /opt/gradle.zip
https://services.gradle.org/distributions/gradle-4.5.1-bin.zip && \  
unzip /opt/gradle.zip -d /opt/ && \  
rm -f /opt/gradle.zip && \  
mv /opt/gradle-* /opt/gradle/  
#  
# INSTALL AND CONFIGURE  
#  
COPY docker-entrypoint-hook.sh /opt/docker-entrypoint-hook.sh  
RUN chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint-hook.sh  
  
#  
# USER: normal  
#  
USER jenkins  
  
#  
# RUN  
#  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:/opt/atlassian-plugin-
sdk-${ATLS_VERSIN}/bin/:/opt/jdk/bin:/opt/gradle/bin:/opt/apache-maven/bin  
USER jenkins  

