FROM maven:3.5.2-jdk-8 as war-build  
  
LABEL license="Apache License, Version 2.0"  
LABEL copyright="CS Systèmes d'Information"  
LABEL maintainer="contact@ikats.org"  
LABEL version="0.7.39"  
  
WORKDIR /usr/src/app  
# /root/.m2 is a volume :(  
# Build cache fix provided by https://github.com/carlossg/docker-
maven/issues/36#issuecomment-334562850  
ENV MAVEN_OPTS=-Dmaven.repo.local=../m2repo/  
  
## Step 1 -- Build the TDM project artifacts and install them into the maven
local repository  
# Add only the maven pom.xml  
# this will help us to cache the maven repository into docker cache  
COPY ikats-datamodel/ikats-datamodel/pom.xml ikats-datamodel/ikats-
datamodel/pom.xml  
COPY ikats-datamodel/ikats-commons/pom.xml ikats-datamodel/ikats-
commons/pom.xml  
COPY ikats-datamodel/dbWebclient/pom.xml ikats-datamodel/dbWebclient/pom.xml  
COPY ikats-datamodel/TemporalDataManagerWebApp/pom.xml ikats-
datamodel/TemporalDataManagerWebApp/pom.xml  
COPY ikats-datamodel/pom.xml ikats-datamodel/pom.xml  
  
# get all the downloads out of the way  
RUN mvn -B -e -C -T 1C org.apache.maven.plugins:maven-dependency-
plugin:3.0.2:go-offline --fail-never -f ikats-datamodel/pom.xml  
#RUN mvn -B -e -o -T 1C verify -f ikats-datamodel/pom.xml  
# Now add the other sources and package the whole into the WAR  
COPY ikats-datamodel/ikats-datamodel ikats-datamodel/ikats-datamodel  
COPY ikats-datamodel/ikats-commons ikats-datamodel/ikats-commons  
COPY ikats-datamodel/dbWebclient ikats-datamodel/dbWebclient  
COPY ikats-datamodel/TemporalDataManagerWebApp ikats-
datamodel/TemporalDataManagerWebApp  
RUN mvn clean install -DskipTests=true -f ikats-datamodel/pom.xml  
  
## Step 2 -- Build the IKATS Ingestion app  
COPY pom.xml .  
RUN mvn -B -e -C -T 1C org.apache.maven.plugins:maven-dependency-
plugin:3.0.2:go-offline --fail-never  
  
COPY LICENSE .  
COPY NOTICE .  
COPY src src  
RUN mvn -B -e -o -T 1C clean package -DskipTests=true  
  
#  
# Creates the Docker image for installing the IKATS Ingestion Service  
#  
# Dockerfile original source from https://github.com/docker-
library/docs/tree/master/tomee  
# Flavor : 8-jdk-7.0.1-plume (8-jdk-7.0.1-plume/Dockerfile)  
FROM openjdk:8  
LABEL license="Apache License, Version 2.0"  
LABEL copyright="CS Systèmes d'Information"  
LABEL maintainer="contact@ikats.org"  
LABEL version="0.7.39"  
  
# install zip in order to repack war after configuration injection  
RUN apt-get update && apt-get install -y --no-install-recommends zip \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/local/tomee/bin:$PATH  
RUN mkdir -p /usr/local/tomee  
  
WORKDIR /usr/local/tomee  
  
RUN set -x \  
&& curl -fsSL 'https://www.apache.org/dist/tomee/KEYS' -o KEYS \  
&& gpg --import KEYS  
  
RUN set -x \  
&& curl -fSL http://repo.maven.apache.org/maven2/org/apache/tomee/apache-
tomee/7.0.4/apache-tomee-7.0.4-plume.tar.gz.asc -o tomee.tar.gz.asc \  
&& curl -fSL http://repo.maven.apache.org/maven2/org/apache/tomee/apache-
tomee/7.0.4/apache-tomee-7.0.4-plume.tar.gz -o tomee.tar.gz \  
&& gpg --batch --verify tomee.tar.gz.asc tomee.tar.gz \  
&& tar -zxf tomee.tar.gz \  
&& mv apache-tomee-plume-7.0.4/* /usr/local/tomee \  
&& rm -Rf apache-tomee-plume-7.0.4 \  
&& rm bin/*.bat \  
&& rm tomee.tar.gz*  
  
# Copy the modified configuration for IKATS  
COPY assets/tomee-conf/. .  
  
# Reclaim the war package at the previous multi-stage  
COPY \--from=war-build /usr/src/app/target/ikats-ingestion.war webapps/.  
  
WORKDIR /tmp/container_init  
COPY assets/container_init.sh .  
COPY assets/inject_configuration.sh .  
  
# Declare a shared volume  
VOLUME ["/mnt/IKATSDATA"]  
  
# Expose functional and debug ports  
EXPOSE 8081 9010 9011  
# Run a script to replace target dependent values into the templated war
configuration  
# and launch the Tomcat  
ENTRYPOINT ["sh", "container_init.sh"]  
  

