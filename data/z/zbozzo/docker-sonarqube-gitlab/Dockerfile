FROM sonarqube:latest  
  
MAINTAINER bozzo  
  
ENV GITLAB_PLUGIN_VERSION 2.0.0  
ENV GITLAB_AUTH_PLUGIN_VERSION 1.2.1  
ENV GITLAB_BADGES_PLUGIN_VERSION 3.0.0  
  
RUN curl -o ${SONARQUBE_HOME}/lib/bundled-plugins/sonar-gitlab-
plugin-${GITLAB_PLUGIN_VERSION}.jar -sSL "https://github.com/gabrie-
allaigre/sonar-gitlab-plugin/releases/download/${GITLAB_PLUGIN_VERSION}/sonar-
gitlab-plugin-${GITLAB_PLUGIN_VERSION}.jar" && \  
curl -o ${SONARQUBE_HOME}/lib/bundled-plugins/sonar-auth-gitlab-
plugin-${GITLAB_AUTH_PLUGIN_VERSION}.jar -sSL "https://github.com/gabrie-
allaigre/sonar-auth-gitlab-
plugin/releases/download/${GITLAB_AUTH_PLUGIN_VERSION}/sonar-auth-gitlab-
plugin-${GITLAB_AUTH_PLUGIN_VERSION}.jar" && \  
curl -o ${SONARQUBE_HOME}/lib/bundled-plugins/qualinsight-plugins-sonarqube-
badges-${GITLAB_BADGES_PLUGIN_VERSION}.jar -sSL
"https://github.com/QualInsight/qualinsight-plugins-sonarqube-
badges/releases/download/qualinsight-plugins-sonarqube-
badges-${GITLAB_BADGES_PLUGIN_VERSION}/qualinsight-sonarqube-
badges-${GITLAB_BADGES_PLUGIN_VERSION}.jar"  

