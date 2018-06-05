# Licensed to the Apache Software Foundation (ASF) under one or more  
# contributor license agreements. See the NOTICE file distributed with  
# this work for additional information regarding copyright ownership.  
# The ASF licenses this file to You under the Apache License, Version 2.0  
# (the "License"); you may not use this file except in compliance with  
# the License. You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
# If this scripted is run out of /usr/bin or some other system bin directory  
# it should be linked to and not copied. Things like java jar files are found  
# relative to the canonical path of this script.  
#  
FROM java:openjdk-8-jre  
MAINTAINER Minoru Osuka "minoru.osuka@gmail.com"  
RUN apt-get update \  
&& apt-get install -y tar ant jq \  
&& apt-get clean  
  
# Add group  
ENV BANANA_GROUP banana  
RUN groupadd -r ${BANANA_GROUP}  
  
# Add user  
ENV BANANA_USER banana  
ENV BANANA_UID 8080  
RUN useradd -r -u ${BANANA_UID} -g ${BANANA_GROUP} ${BANANA_USER}  
  
ENV INSTALL_DIR=/opt  
RUN mkdir -p ${INSTALL_DIR}  
  
# Install Jetty  
ENV JETTY_VERSION 9.3.8.v20160314  
WORKDIR ${INSTALL_DIR}  
RUN curl -L -o ${INSTALL_DIR}/jetty-distribution-${JETTY_VERSION}.tar.gz
http://download.eclipse.org/jetty/${JETTY_VERSION}/dist/jetty-
distribution-${JETTY_VERSION}.tar.gz  
RUN tar -xzf jetty-distribution-${JETTY_VERSION}.tar.gz && rm
${INSTALL_DIR}/jetty-distribution-${JETTY_VERSION}.tar.gz  
ENV JETTY_PREFIX ${INSTALL_DIR}/jetty-distribution-${JETTY_VERSION}  
RUN chown -R ${BANANA_USER}:${BANANA_GROUP} ${JETTY_PREFIX}  
  
# Install Banana  
# ENV BANANA_VERSION release-1.6.0  
ENV BANANA_VERSION release  
WORKDIR ${INSTALL_DIR}  
# RUN curl -L -o ${INSTALL_DIR}/banana-${BANANA_VERSION}.zip
https://github.com/lucidworks/banana/archive/${BANANA_VERSION}.zip  
RUN curl -L -o ${INSTALL_DIR}/banana-${BANANA_VERSION}.zip
https://github.com/mosuka/banana/archive/${BANANA_VERSION}.zip  
RUN unzip banana-${BANANA_VERSION}.zip && rm
${INSTALL_DIR}/banana-${BANANA_VERSION}.zip  
ENV BANANA_PREFIX ${INSTALL_DIR}/banana-${BANANA_VERSION}  
RUN chown -R ${BANANA_USER}:${BANANA_GROUP} ${BANANA_PREFIX}  
WORKDIR ${BANANA_PREFIX}  
RUN ant -Dfinal.name=banana  
RUN cp ${BANANA_PREFIX}/build/banana.war ${JETTY_PREFIX}/webapps/.  
  
# Add start and stop script  
ADD docker-run.sh /usr/local/bin/  
ADD docker-stop.sh /usr/local/bin/  
  
ENV JETTY_HTTP_PORT=5601  
EXPOSE 5601  
USER ${BANANA_USER}  
  
WORKDIR ${JETTY_PREFIX}  
  
CMD ["/usr/local/bin/docker-run.sh"]  

