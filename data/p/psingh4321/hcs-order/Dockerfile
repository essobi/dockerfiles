FROM java:8-jdk  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV JAVA_OPTS ""  
ENV PATH $PATH:$JAVA_HOME/bin  
  
ARG MAVEN_VERSION=3.5.2  
ARG USER_HOME_DIR="/root"  
ARG SHA=707b1f6e390a65bde4af4cdaf2a24d45fc19a6ded00fff02e91626e3e42ceaff  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV PATH $PATH:$MAVEN_HOME/bin  
  
# Prepare app directory  
RUN mkdir -p /usr/src/app  
RUN mkdir -p /usr/src/app/log  
ADD . /usr/src/app  
  
# Install dependencies  
WORKDIR /usr/src/app  
  
RUN mvn clean install  
  
# Tell Docker about the port we'll run on.  
EXPOSE 8060  
# CMD java $JAVA_OPTS -jar /usr/src/app/target/hcs-order-0.0.1-SNAPSHOT.jar >
/usr/src/app/log/logger.log  
ENTRYPOINT ["java", "-Dlogging.file=SystemOut.log", "-jar",
"/usr/src/app/target/hcs-order-0.0.1-SNAPSHOT.jar", "--
spring.config.location=classpath:/application-prod.properties", "--
server.port=8060"]

