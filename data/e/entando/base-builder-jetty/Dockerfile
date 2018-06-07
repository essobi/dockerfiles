FROM openjdk:8-slim  
  
#Environment Variables  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
ENV JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre  
ENV MAVEN_HOME=/usr/share/maven  
ENV PROJECT_HOME=/opt/entando  
ENV MVN_HOME=${PROJECT_HOME}/.m2  
  
RUN apt-get update && apt-get install --no-install-recommends -y maven
imagemagick git \  
&& apt-get autoclean -y \  
&& mkdir -p ${PROJECT_HOME} && mkdir -p ${PROJECT_HOME}/.m2/repository &&
chown -R 1001:0 ${PROJECT_HOME}/ && chmod -R ug+w ${PROJECT_HOME}/  
  
COPY settings.xml ${MAVEN_HOME}/conf/settings.xml  
  
WORKDIR ${PROJECT_HOME}  
  
# Install entando dependencies (archetypes) from master branch  
# Set local maven repository to /opt/entando/.m2/repository  
# Create a symbolic link to archetype-catalog.xml file in repository directory
to have local archetypes updated  
RUN cd ${PROJECT_HOME} \  
&& git clone https://github.com/entando/entando-archetypes.git \  
&& cd ${PROJECT_HOME}/entando-archetypes && mvn
-Dmaven.repo.local=${MVN_HOME}/repository install \  
&& chown -R 1001:0 ${MVN_HOME}/ && chmod -R ug+w ${MVN_HOME}/ \  
&& rm -rf ${PROJECT_HOME}/entando-*

