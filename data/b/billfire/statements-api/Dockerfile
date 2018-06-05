  
FROM openjdk:8-jdk  
  
ARG AWS_ACCESS_KEY_ID  
ARG AWS_SECRET_ACCESS_KEY  
  
ARG MAVEN_VERSION=3.5.3  
ARG USER_HOME_DIR="/root"  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y zip  
  
ENV DEBIAN_FRONTEND teletype  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
ADD / .  
RUN mvn dependency:go-offline  
RUN mvn install spring-boot:repackage

