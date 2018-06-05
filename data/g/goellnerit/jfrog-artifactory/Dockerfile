FROM docker.bintray.io/jfrog/artifactory-oss:5.3.1  
MAINTAINER philipp.goellner@xaltbc.de  
  
# Timezone (for correct logging date)  
ENV TIME_ZONE Europe/Berlin  
  
# Environment variables for container initialization  
ENV INIT_DIRECTORY /docker/artifactory/init  
ENV TEMP_DIRECTORY /docker/artifactory/temp  
  
# Create init and temp directory  
RUN mkdir -p ${INIT_DIRECTORY} \  
&& mkdir -p ${TEMP_DIRECTORY}  
  
# Copy start script and set correct permissions  
COPY init/* ${INIT_DIRECTORY}/  
RUN chmod 740 ${INIT_DIRECTORY}/*.sh  
  
# Install necessary packages  
RUN apt-get update --quiet \  
&& apt-get install -y --quiet openssh-client \  
rsync \  
&& apt-get clean  
  
VOLUME ["${ARTIFACTORY_DATA}"]  
  
# Execute start script  
ENTRYPOINT ["/docker/artifactory/init/configure-and-start.sh"]  

