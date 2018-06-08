FROM goodrainapps/openjdk:8u131-jdk-alpine  
  
MAINTAINER zhouyq@goodrain.com  
  
# Set vars  
ENV ARTIFACTORY_USER_NAME=artifactory \  
ARTIFACTORY_USER_ID=200 \  
ARTIFACTORY_HOME=/opt/jfrog/artifactory \  
ARTIFACTORY_DATA=/var/opt/jfrog/artifactory \  
RECOMMENDED_MAX_OPEN_FILES=32000 \  
MIN_MAX_OPEN_FILES=10000 \  
RECOMMENDED_MAX_OPEN_PROCESSES=1024 \  
POSTGRESQL_VERSION=9.4.1212  
  
ENV ARTIFACTORY_VER=5.4.6 \  
DOWNLOAD_URL="https://bintray.com/jfrog/artifactory/download_file?file_path="  
RUN set -ex \  
&& mkdir -pv /opt/jfrog \  
&& curl -sL -o /opt/jfrog/artifactory-oss.zip ${DOWNLOAD_URL}jfrog-
artifactory-oss-${ARTIFACTORY_VER}.zip \  
&& unzip -q /opt/jfrog/artifactory-oss.zip -d /opt/jfrog/ \  
&& mv ${ARTIFACTORY_HOME}-oss-${ARTIFACTORY_VER}/ ${ARTIFACTORY_HOME}/ \  
&& rm -rf ${ARTIFACTORY_HOME}/etc ${ARTIFACTORY_HOME}/logs
/opt/jfrog/artifactory-oss.zip\  
&& sed -i "s/nofiles/${ARTIFACTORY_USER_NAME}/" /etc/group \  
&& adduser -u ${ARTIFACTORY_USER_ID} -D -S -G ${ARTIFACTORY_USER_NAME}
${ARTIFACTORY_USER_NAME} \  
&& chown -R ${ARTIFACTORY_USER_NAME}:${ARTIFACTORY_USER_NAME}
${ARTIFACTORY_HOME}  
  
COPY entrypoint-artifactory.sh /  
RUN chmod +x /entrypoint-artifactory.sh  
# Default mounts. Should be passed in `docker run` or in docker-compose  
VOLUME /var/opt/jfrog/artifactory  
  
# Expose Tomcat's port  
EXPOSE 8081  
  
# Start the simple standalone mode of Artifactory  
ENTRYPOINT /entrypoint-artifactory.sh  

