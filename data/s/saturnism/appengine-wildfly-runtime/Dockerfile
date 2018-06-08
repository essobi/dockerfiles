# Copyright 2014 Google Inc.  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
FROM google/debian:wheezy  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && \  
apt-get install --no-install-recommends -y --force-yes -q ca-certificates curl
openjdk-7-jre-headless && \  
apt-get clean && \  
rm /var/lib/apt/lists/*_*  
  
ENV WILDFLY_HOME /var/lib/wildfly  
ENV WILDFLY_VERSION 8.2.0.Final  
RUN mkdir -p ${WILDFLY_HOME} && (curl -0
http://download.jboss.org/wildfly/${WILDFLY_VERSION}/wildfly-${WILDFLY_VERSION}.tar.gz
| tar -C ${WILDFLY_HOME} \--strip-components=1 -zx)  
  
ENV APPENGINE_VERSION 1.9.18  
ENV JGROUPS_VERSION 3.6.2.Final  
  
RUN cd /tmp/ && curl -0 \  
-O http://repo1.maven.org/maven2/com/google/appengine/appengine-api-1.0-sdk/${APPENGINE_VERSION}/appengine-api-1.0-sdk-${APPENGINE_VERSION}.jar \  
-O https://oss.sonatype.org/content/repositories/google-releases/com/google/appengine/appengine-managed-runtime/${APPENGINE_VERSION}/appengine-managed-runtime-${APPENGINE_VERSION}.jar  
  
ADD . ${WILDFLY_HOME}  
  
RUN mv /tmp/appengine-*.jar ${WILDFLY_HOME}/modules/com/google/appengine/main/  
RUN sed -i "s/\$APPENGINE_VERSION/${APPENGINE_VERSION}/g"
${WILDFLY_HOME}/modules/com/google/appengine/main/module.xml  
  
RUN sed -i '/<dependencies>/a <module name="org.jgroups.googleping"\/>'
${WILDFLY_HOME}/modules/system/layers/base/org/jgroups/main/module.xml  
RUN sed -i '/<dependencies>/a <module name="org.jgroups.googleping"\/>'
${WILDFLY_HOME}/modules/system/layers/base/org/jboss/as/clustering/jgroups/main/module.xml  
  
RUN ln -s ${WILDFLY_HOME}/standalone/deployments /deployments  
WORKDIR /deployments  
  
# Wildfly HTTP port number  
EXPOSE 8080  
# Wildfly HTTP Admin port number  
EXPOSE 9990  
# Widlfy JGroups Ports  
EXPOSE 7600  
EXPOSE 57600  
# Java VM debug port number  
EXPOSE 5005  
# Env variable used by the jetty_run.sh script  
ENV RUNTIME_DIR ${WILDFLY_HOME}  
  
# Clean any CMD that might be inherited from previous image, because that  
# will pollute our ENTRYPOINT, see  
# http://docs.docker.io/en/latest/reference/builder/#entrypoint.  
CMD []  
VOLUME ["/var/log/app_engine"]  
ENTRYPOINT ["/var/lib/wildfly/wildfly_run.sh"]  

