FROM docker.bintray.io/jfrog/artifactory-pro:5.5.1  
ENV PG_PLUGIN_VERSION 9.4.1212  
ENV DOWNLOAD_PG_PLUGIN_URL
https://jdbc.postgresql.org/download/postgresql-${PG_PLUGIN_VERSION}.jar  
  
# postgres plugin  
RUN curl -SL "${DOWNLOAD_PG_PLUGIN_URL}" \--create-dirs -o
"/opt/jfrog/artifactory/tomcat/lib/postgresql-${PG_PLUGIN_VERSION}.jar"  
  
RUN set -x \  
&& cd /opt/jfrog/artifactory \  
&& curl -SLO
"https://gist.github.com/khorevaa/53758daac0d1f1afd43b995f185a337d/raw/0cd76e8335b3583b6d03914071f3d3eb5608baca/ArtifactoryProInjector.jar"
\  
&& java -jar ArtifactoryProInjector.jar /opt/jfrog/artifactory  
  
MAINTAINER Khorevaa@gmail.com  

