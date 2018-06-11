FROM buildpack-deps:sid-scm  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /jdk-9  
RUN curl -o /tmp/jdk.tar.gz
http://download.java.net/java/GA/jdk9/9/binaries/jdk-9+181_linux-x64_bin.tar.gz  
RUN tar -xvzf /tmp/jdk.tar.gz -C /  
RUN ln -s $JAVA_HOME/bin/java /usr/bin/java  
  
ARG MAVEN_VERSION=3.5.0  
ARG USER_HOME_DIR="/root"  
ARG SHA=beb91419245395bd69a4a6edad5ca3ec1a8b64e41457672dc687c173a495f034  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
COPY settings-docker.xml /usr/share/maven/ref/  
  
RUN chmod +x /usr/local/bin/mvn-entrypoint.sh  
  
VOLUME "$USER_HOME_DIR/.m2"  
  
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]  
CMD ["mvn"]

