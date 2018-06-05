#official image name: fkirill/artifactory  
FROM tomcat:8-jre8  
  
# based on existing repository https://github.com/mattgruter/dockerfile-
artifactory  
MAINTAINER Kirill Frolov <kirill.frolov@servian.com>  
  
# To update, check https://bintray.com/jfrog/artifactory/artifactory/view  
ENV ARTIFACTORY_VERSION 4.1.2  
ENV ARTIFACTORY_SHA1 245aeb7b2d77830462067d5a19c3bd32ae014ddf  
  
# Sharing home folder to allow run as non-root later  
RUN chmod -R 777 . *  
  
# Artifactory home  
RUN mkdir -p /artifactory/data /artifactory/logs /artifactory/backup  
RUN chmod 777 -R /artifactory  
COPY urlrewrite/WEB-INF/lib/urlrewritefilter.jar /  
COPY urlrewrite/WEB-INF/urlrewrite.xml /  
RUN chmod 777 /*urlrewrite*  
  
# Running under non-root user to allow non-privileged container execution  
USER 1001  
# Disable Tomcat's manager application.  
RUN rm -rf webapps/*  
  
# Expose tomcat runtime options through the RUNTIME_OPTS environment variable.  
# Example to set the JVM's max heap size to 256MB use the flag  
# '-e RUNTIME_OPTS="-Xmx256m"' when starting a container.  
RUN echo 'export CATALINA_OPTS="$RUNTIME_OPTS"' > bin/setenv.sh  
  
RUN rm -rf webapps/*  
  
# Redirect URL from / to artifactory/ using UrlRewriteFilter  
RUN \  
mkdir -p webapps/ROOT/WEB-INF/lib && \  
cp /urlrewritefilter.jar webapps/ROOT/WEB-INF/lib && \  
cp /urlrewrite.xml webapps/ROOT/WEB-INF/  
  
# Fetch and install Artifactory OSS war archive.  
RUN \  
curl -L -o artifactory.zip
https://bintray.com/artifact/download/jfrog/artifactory/jfrog-artifactory-
oss-${ARTIFACTORY_VERSION}.zip && \  
unzip -j artifactory.zip "artifactory-*/webapps/artifactory.war" -d webapps &&
\  
rm artifactory.zip  
  
ENV ARTIFACTORY_HOME /artifactory  
  
# Expose Artifactories data, log and backup directory.  
VOLUME /artifactory/data  
VOLUME /artifactory/logs  
VOLUME /artifactory/backup  
  
WORKDIR /artifactory  

