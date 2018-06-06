FROM openjdk:8-jdk-alpine  
  
ARG MAVEN_VERSION=3.3.9  
RUN apk add --no-cache curl tar jq bash \  
&& mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL $(wget -q -O - "http://www.apache.org/dyn/closer.cgi?as_json=1"
| jq -r .preferred)/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& ls -lrt #rm apache-maven-$MAVEN_VERSION-bin.tar.gz \  
&& rm -rf /var/cache/apk/*  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG /usr/share/maven/ref  
ENV COPY_REFERENCE_FILE_LOG $MAVEN_CONFIG/copy_reference_file.log  
  
COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
COPY settings-docker.xml /usr/share/maven/ref/  
  
COPY settings.xml /usr/share/maven/ref/  
COPY pom.xml /tmp/pom.xml  
RUN mvn -B -f /tmp/pom.xml -s /usr/share/maven/ref/settings-docker.xml
dependency:resolve  

