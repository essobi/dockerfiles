# Maven v3.3  
# docker run --rm pottava/maven:3.3-java7  
  
FROM pottava/java:7  
  
ENV MAVEN_VERSION=3.3.9 \  
MAVEN_HOME=/opt/maven \  
JAVA_HOME=/usr/lib/jvm/java-1.7-openjdk/jre  
  
RUN set -ex \  
&& apk --no-cache add --virtual build-dependencies wget \  
&& cd /tmp \  
&& wget --quiet
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -O - | tar xzf - \  
&& mv /tmp/apache-maven-$MAVEN_VERSION /usr/lib/maven \  
&& ln -s /usr/lib/maven/bin/mvn /usr/bin/mvn \  
&& rm -rf /tmp/* \  
&& apk del --purge build-dependencies  
  
CMD ["/usr/bin/mvn", "-v"]  

