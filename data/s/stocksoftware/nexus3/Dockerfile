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
#  
FROM stocksoftware/java:jdk8  
  
# configure nexus runtime  
ENV NEXUS_VERSION=3.2.1-01 \  
SONATYPE_DIR=/opt/sonatype  
  
# Setup nexus user and group  
# Install nexus into /opt/sonatype/nexus  
# Configure nexus runtime  
# Setup nexus data directory  
ENV NEXUS_HOME=${SONATYPE_DIR}/nexus \  
NEXUS_DATA=/nexus-data \  
NEXUS_CONTEXT='' \  
SONATYPE_WORK=${SONATYPE_DIR}/sonatype-work \  
NEXUS_DOWNLOAD_URL=https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz  
  
RUN adduser -D -H -s /bin/false -h ${NEXUS_DATA} -u 200 -S nexus && \  
addgroup -S nexus -g 600 && \  
mkdir -p ${SONATYPE_DIR} && \  
cd /tmp && \  
mkdir -p /opt/sonatype && \  
curl --fail --silent --location --retry 3 ${NEXUS_DOWNLOAD_URL} > nexus.tar.gz
&& \  
tar xzf nexus.tar.gz && \  
mv nexus-${NEXUS_VERSION} ${NEXUS_HOME} && \  
rm nexus.tar.gz && \  
sed \  
-e '/^nexus-context/ s:$:${NEXUS_CONTEXT}:' \  
-i ${NEXUS_HOME}/etc/nexus-default.properties && \  
mkdir -p ${NEXUS_DATA}/etc ${NEXUS_DATA}/log ${NEXUS_DATA}/tmp
${SONATYPE_WORK} && \  
ln -s ${NEXUS_DATA} ${SONATYPE_WORK}/nexus3 && \  
chown -R nexus:nexus ${NEXUS_DATA} && \  
chown -R nexus:nexus ${SONATYPE_WORK} && \  
chown -R root:root ${NEXUS_HOME}  
  
VOLUME ${NEXUS_DATA}  
  
EXPOSE 8081  
USER nexus:nexus  
  
WORKDIR /opt/sonatype/nexus  
  
ENV JAVA_MAX_MEM=1200m \  
JAVA_MIN_MEM=1200m \  
EXTRA_JAVA_OPTS=""  
CMD ["/opt/sonatype/nexus/bin/nexus","run"]  

