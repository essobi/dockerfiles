#  
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
# Start from JDK 8 based on Alpine Linux image (~5Mb)  
FROM openjdk:8-jre-alpine  
  
# Set Product name  
ENV PRODUCT gridgain  
# Set GridGain version  
ENV GRIDGAIN_VERSION 8.4.4  
# Set GridGain edition  
ENV GRIDGAIN_EDITION ultimate  
# Set Ignite binary name  
ENV GRIDGAIN_BIN ${PRODUCT}-${GRIDGAIN_EDITION}-fabric-${GRIDGAIN_VERSION}  
# Set Ignite home directory  
ENV IGNITE_HOME /opt/${PRODUCT}/${GRIDGAIN_BIN}  
  
# Set working directory  
WORKDIR /opt/${PRODUCT}  
  
# Add missing software  
RUN apk --update add \  
bash \  
&& rm -rfv /var/cache/apk/*  
  
# Get binary archive  
RUN set -x && \  
wget -c "https://gridgain.com/media/${GRIDGAIN_BIN}.zip" -O gridgain.zip && \  
unzip gridgain.zip && \  
rm -rfv gridgain.zip  
  
# Copy sh files and set permission  
COPY ./run.sh ${IGNITE_HOME}/  
  
CMD ${IGNITE_HOME}/run.sh  
  
EXPOSE 11211 47100 47500 49112  

