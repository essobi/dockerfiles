#  
# Copyright (c) 2018 The Hyve B.V.  
# This code is licensed under the GNU Affero General Public License (AGPL),  
# version 3, or (at your option) any later version.  
#  
FROM openjdk:8  
LABEL maintainers=" \  
Pieter Lukasse (The Hyve) <pieter@thehyve.nl>, \  
Oleguer Plantalech Casals (The Hyve) <oleguer@thehyve.nl> \  
"  
  
# install build and runtime dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
maven \  
python \  
python-pip && \  
pip install setuptools && \  
pip install awscli --upgrade --user && \  
apt-get purge -y --auto-remove python-pip && \  
apt-get purge -y --auto-remove python  
  
# install dependency for running docker client in this container  
RUN apt-get update && apt-get install -y libltdl7 && rm -rf
/var/lib/apt/lists/*  
  
# get code  
ENV STAGING_HOME=/cbioportal-staging  
COPY . $STAGING_HOME  
WORKDIR $STAGING_HOME  
  
# prepare application.properties, so that this is take by default by spring
framework  
RUN cp $STAGING_HOME/src/main/resources/application.properties.EXAMPLE
$STAGING_HOME/src/main/resources/application.properties  
  
# maven build and rename .jar (excluding full integration test here as this
executes docker commands and  
# is meant to run on CI environment only)  
RUN mvn clean install -Dcbioportal-
staging.test.excludes="**/*FullIntegration*.java" && \  
mv $STAGING_HOME/target/cbioportal-staging-*.jar
$STAGING_HOME/target/cbioportal-staging.jar  
  
# service to be started with default properties (can be overridden in docker
run),  
# taking also custom properties, if given at default -v location  
ENTRYPOINT ["/cbioportal-staging/target/cbioportal-staging.jar", "--
spring.config.location=file:///custom/custom.properties"]  

