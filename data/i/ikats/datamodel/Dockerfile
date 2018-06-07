FROM maven:3.5.2-jdk-8 as war-build  
  
WORKDIR /srcs  
  
# Add only the maven pom.xml  
# this will help us to cache the maven repository into docker cache  
COPY ikats-datamodel/pom.xml ikats-datamodel/pom.xml  
COPY ikats-commons/pom.xml ikats-commons/pom.xml  
COPY dbWebclient/pom.xml dbWebclient/pom.xml  
COPY TemporalDataManagerWebApp/pom.xml TemporalDataManagerWebApp/pom.xml  
COPY pom.xml .  
  
# get all the downloads out of the way  
RUN mvn verify --fail-never  
  
# Now add the other sources and package the whole into the WAR  
COPY LICENSE .  
COPY NOTICE .  
COPY ikats-datamodel ikats-datamodel  
COPY ikats-commons ikats-commons  
COPY dbWebclient dbWebclient  
COPY TemporalDataManagerWebApp TemporalDataManagerWebApp  
  
# Compile and package the WAR  
RUN mvn clean package -DskipTests=true  
  
# Multi-stage build to not retain the previous intermediate build work in our
image  
# Reference: https://docs.docker.com/develop/develop-images/multistage-build/  
FROM tomcat:8.5.8-alpine  
  
LABEL license="Apache License, Version 2.0"  
LABEL copyright="CS Systèmes d'Information"  
LABEL maintainer="contact@ikats.org"  
LABEL version="0.7.39"  
  
ADD assets/context.xml /usr/local/tomcat/conf/  
ADD assets/context.xml /usr/local/tomcat/webapps/manager/META-INF  
ADD assets/context.xml /usr/local/tomcat/webapps/host-manager/manager.xml  
  
# Reclaim the build WAR to put it into tomcat working directory for immediate
deployement  
WORKDIR /usr/local/tomcat/  
COPY \--from=war-build
/srcs/TemporalDataManagerWebApp/target/TemporalDataManagerWebApp.war webapps/.  
  
# Add zip utility for packing the war  
RUN apk add --update zip  
  
WORKDIR /tmp/container_init  
COPY assets/container_init.sh .  
COPY assets/inject_configuration.sh .  
  
# Run a script to replace target dependent values into the templated war
configuration  
# and launch the Tomcat  
ENTRYPOINT ["sh", "container_init.sh"]  

