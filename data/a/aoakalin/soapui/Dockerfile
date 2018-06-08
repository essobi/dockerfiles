FROM cogniteev/oracle-java:java7  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV MAVEN_DOWNLOAD_URL
https://apache.osuosl.org/maven/maven-3/3.5.0/binaries/apache-
maven-3.5.0-bin.tar.gz  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
ENV SOAPUI_VERSION 5.3.0  
ENV SOAPUI_TAR_NAME SoapUI-${SOAPUI_VERSION}-linux-bin.tar.gz  
ENV SOAPUI_DOWNLOAD_URL
http://cdn01.downloads.smartbear.com/soapui/${SOAPUI_VERSION}/${SOAPUI_TAR_NAME}  
ENV SOAPUI_PATH /var/soapui  
ENV SOAPUI_HOME ${SOAPUI_PATH}/SoapUI-${SOAPUI_VERSION}  
ENV SOAPUI_PROJECTS ${SOAPUI_PATH}/projects  
ENV SOAPUI_MOCK_PORT 8080  
ENV PATH ${PATH}:${SOAPUI_HOME}/bin  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
curl \  
subversion \  
git \  
&& mkdir -p "${SOAPUI_HOME}" \  
&& mkdir -p "${SOAPUI_PROJECTS}" \  
&& cd "${SOAPUI_PATH}" \  
&& wget "${SOAPUI_DOWNLOAD_URL}" \  
&& tar -zxvf "${SOAPUI_TAR_NAME}" \  
&& rm -f "${SOAPUI_TAR_NAME}" \  
&& mkdir -p "${MAVEN_HOME}/ref" \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz "${MAVEN_DOWNLOAD_URL}" \  
&& tar -xzf /tmp/apache-maven.tar.gz -C "${MAVEN_HOME}" \--strip-components=1
\  
&& ln -s "${MAVEN_HOME}/bin/mvn" /usr/bin/mvn \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /tmp/apache-maven.tar.gz  
  
COPY ["docker-entrypoint.sh", "${SOAPUI_PATH}/docker-entrypoint.sh"]  
RUN chmod +x "${SOAPUI_PATH}/docker-entrypoint.sh"  
  
WORKDIR "${SOAPUI_PATH}"  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD tail -f /dev/null  
EXPOSE ${SOAPUI_MOCK_PORT}  
  
VOLUME "${MAVEN_CONFIG}"  
VOLUME "${SOAPUI_HOME}"  
VOLUME "${SOAPUI_PROJECTS}"  

