FROM java:8  
MAINTAINER Niek Palm "dev.npalm@gmail.com"  
ENV ARTIFACTORY_HOME /artifactory  
ENV ARTIFACTORY_VERSION 4.7.1  
#ENV ARTIFACTORY_URL
http://dl.bintray.com/content/jfrog/artifactory/artifactory-$ARTIFACTORY_VERSION.zip?direct  
ENV ARTIFACTORY_URL
https://bintray.com/artifact/download/jfrog/artifactory/jfrog-artifactory-
oss-$ARTIFACTORY_VERSION.zip?direct  
  
ADD $ARTIFACTORY_URL /artifactory.zip  
RUN unzip /artifactory.zip -d / \  
&& mv /artifactory-oss-${ARTIFACTORY_VERSION} /artifactory \  
&& rm -f /artifactory.zip  
  
# Change memory settings  
RUN sed -i -e 's/Xmx2g/Xmx512m/g' /artifactory/bin/artifactory.default  
  
# Expose the default endpoint  
EXPOSE 8081  
VOLUME ["/artifactory/data", "/artifactory/backup", "/artifactory/logs"]  
  
# Run the embedded tomcat container  
ENTRYPOINT /artifactory/bin/artifactory.sh  

