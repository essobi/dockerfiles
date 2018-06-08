# Builds a docker image for the Confluent schema registry.  
# Expects links to "kafka" and "zookeeper" containers.  
#  
# Usage:  
# docker build -t confluent/schema-registry schema-registry  
# docker run -d --name schema-registry --link zookeeper:zookeeper --link
kafka:kafka \  
# --env SCHEMA_REGISTRY_AVRO_COMPATIBILITY_LEVEL=none confluent/schema-
registry  
FROM java:openjdk-8-jdk-alpine  
  
RUN MAVEN_VERSION=3.3.3 \  
&& cd /usr/share \  
&& wget -q -O -
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | \  
tar xzf - \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
ARG VERSION=2.0.1  
ARG MIRROR=https://github.com/confluentinc/schema-registry/archive  
  
ENV SCHEMA_REGISTRY_HOME /opt/schema-registry  
ENV PATH $PATH:$SCHEMA_REGISTRY_HOME/bin  
  
RUN mkdir /opt  
RUN mkdir /logs  
  
# Dependencies  
RUN apk add --no-cache supervisor bash openssl curl  
  
#Get Schema Registry  
RUN wget -q -O - $MIRROR/v$VERSION.tar.gz | \  
tar -xzf - -C /opt && \  
mv /opt/schema-registry-$VERSION /opt/schema-registry  
RUN cd /opt/schema-registry; \  
mvn clean package -DskipTests  
  
#Copy files  
ADD supervisor.ini /etc/supervisor.d/supervisor.ini  
ADD schema-registry-docker.sh /usr/bin/  
ADD schema-registry.properties /etc/  
  
#TODO Schema Registry needs a log directory.  
USER root  
RUN ["chmod", "+x", "/usr/bin/schema-registry-docker.sh"]  
  
# Supervisor config  
ADD supervisor.ini /etc/supervisor.d/supervisor.ini  
  
EXPOSE 8281  
CMD ["supervisord", "-n", "-c", "/etc/supervisor.d/supervisor.ini"]  

