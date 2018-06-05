#  
# Image for Open DevOps Pipeline  
#  
#VERSION : 0.1  
FROM java:8  
#Maintainer  
MAINTAINER Open DevOps Team <open.devops@gmail.com>  
  
ENV ARTIFACTORY_VERSION=4.9.0 \  
ARTIFACTORY_HOME=/opt/artifactory  
  
# Http port  
EXPOSE 8081  
RUN set -x \  
&& mkdir -p /opt \  
&& cd /opt \  
&& curl -L "http://jfrog.bintray.com/artifactory-
pro/org/artifactory/pro/jfrog-artifactory-pro/${ARTIFACTORY_VERSION}/jfrog-
artifactory-pro-${ARTIFACTORY_VERSION}.zip" -o jfrog-artifactory-
pro-${ARTIFACTORY_VERSION}.zip \  
&& unzip jfrog-artifactory-pro-${ARTIFACTORY_VERSION}.zip \  
&& mv artifactory-pro-${ARTIFACTORY_VERSION} artifactory \  
&& rm jfrog-artifactory-pro-${ARTIFACTORY_VERSION}.zip  
  
#Volume  
WORKDIR $ARTIFACTORY_HOME  
  
ENTRYPOINT ["./bin/artifactory.sh"]  

