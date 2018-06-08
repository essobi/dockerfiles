FROM java:openjdk-8u45-jre  
  
USER root  
ENV SONARQUBE_VERSION 5.0.1  
ENV SONARQUBE_HOME /opt/sonarqube  
  
# Http port  
EXPOSE 9000  
RUN set -x \  
&& cd /opt \  
&& curl -o sonarqube.zip -fSL
https://downloads.sonarsource.com/sonarqube/sonarqube-${SONARQUBE_VERSION}.zip
\  
&& unzip sonarqube.zip \  
&& mv sonarqube-${SONARQUBE_VERSION} sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf ${SONARQUBE_HOME}/bin/*  
  
RUN apt-get install -y wget  
  
# Install bundled-plugins  
RUN ls -la /opt/sonarqube/lib/bundled-plugins  
RUN rm -rf /opt/sonarqube/lib/bundled-plugins/sonar-*-plugin-*.jar  
  
ENV SONAR_JAVA_BUNDLED_PLUGIN_VERSION 2.8  
RUN (cd /opt/sonarqube/lib/bundled-plugins/ && \  
wget --no-check-certificate https://repo1.maven.org/maven2/org/codehaus/sonar-
plugins/java/sonar-java-plugin/${SONAR_JAVA_BUNDLED_PLUGIN_VERSION}/sonar-
java-plugin-${SONAR_JAVA_BUNDLED_PLUGIN_VERSION}.jar)  
  
ENV SONAR_FINDBUGS_BUNDLED_PLUGIN_VERSION 2.4  
RUN (cd /opt/sonarqube/lib/bundled-plugins/ && \  
wget --no-check-certificate https://repo1.maven.org/maven2/org/codehaus/sonar-
plugins/java/sonar-findbugs-
plugin/${SONAR_FINDBUGS_BUNDLED_PLUGIN_VERSION}/sonar-findbugs-
plugin-${SONAR_FINDBUGS_BUNDLED_PLUGIN_VERSION}.jar)  
  
# Install extension plugins  
ENV SONAR_BUILD_BREAKER_PLUGIN_VERSION 1.1  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate https://repo1.maven.org/maven2/org/codehaus/sonar-
plugins/sonar-build-breaker-
plugin/${SONAR_BUILD_BREAKER_PLUGIN_VERSION}/sonar-build-breaker-
plugin-${SONAR_BUILD_BREAKER_PLUGIN_VERSION}.jar)  
  
ENV SONAR_COBERTURA_PLUGIN_VERSION 1.6.3  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate https://repo1.maven.org/maven2/org/codehaus/sonar-
plugins/sonar-cobertura-plugin/${SONAR_COBERTURA_PLUGIN_VERSION}/sonar-
cobertura-plugin-${SONAR_COBERTURA_PLUGIN_VERSION}.jar)  
  
ENV SONAR_FINDBUGS_PLUGIN_VERSION 3.1  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate https://repo1.maven.org/maven2/org/codehaus/sonar-
plugins/java/sonar-findbugs-plugin/${SONAR_FINDBUGS_PLUGIN_VERSION}/sonar-
findbugs-plugin-${SONAR_FINDBUGS_PLUGIN_VERSION}.jar)  
  
ENV SONAR_JAVA_PLUGIN_VERSION 2.6  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate https://repo1.maven.org/maven2/org/codehaus/sonar-
plugins/java/sonar-java-plugin/${SONAR_JAVA_PLUGIN_VERSION}/sonar-java-
plugin-${SONAR_JAVA_PLUGIN_VERSION}.jar)  
  
ENV SONAR_JAVASCRIPT_PLUGIN_VERSION 2.6  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate
https://downloads.sonarsource.com/plugins/org/codehaus/sonar-
plugins/javascript/sonar-javascript-
plugin/${SONAR_JAVASCRIPT_PLUGIN_VERSION}/sonar-javascript-
plugin-${SONAR_JAVASCRIPT_PLUGIN_VERSION}.jar)  
  
ENV SONAR_LDAP_PLUGIN 1.4  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate
https://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-
ldap-plugin/${SONAR_LDAP_PLUGIN}/sonar-ldap-plugin-${SONAR_LDAP_PLUGIN}.jar)  
  
ENV SONAR_SCOVERAGE_PLUGIN_VERSION 4.5.0  
RUN (cd /opt/sonarqube/extensions/plugins/ && \  
wget --no-check-certificate https://github.com/RadoBuransky/sonar-scoverage-
plugin/releases/download/v${SONAR_SCOVERAGE_PLUGIN_VERSION}/sonar-scoverage-
plugin-${SONAR_SCOVERAGE_PLUGIN_VERSION}.jar)  
  
WORKDIR ${SONARQUBE_HOME}  
COPY run.sh ${SONARQUBE_HOME}/bin/  
RUN chmod +x ${SONARQUBE_HOME}/bin/run.sh  
RUN useradd sonar  
RUN chown -R sonar /opt/sonarqube  
ENTRYPOINT ["./bin/run.sh"]  
  

