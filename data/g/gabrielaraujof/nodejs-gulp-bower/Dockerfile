# Pull base image.  
FROM node:6  
LABEL maintainer "Gabriel Araujo <contact@gbiel.com>"  
  
ENV SONAR_SCANNER_VERSION 2.8  
ENV SONAR_SCANNER_HOME /home/sonar-scanner-${SONAR_SCANNER_VERSION}  
ENV SONAR_SCANNER_PACKAGE sonar-scanner-${SONAR_SCANNER_VERSION}.zip  
ENV SONAR_RUNNER_HOME ${SONAR_SCANNER_HOME}  
ENV PATH $PATH:${SONAR_SCANNER_HOME}/bin  
ENV WORKDIR /home/workspace  
  
# Define working directory.  
WORKDIR ${WORKDIR}  
  
# Install dependencies  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get -yqq update && \  
apt-get install -yqq -t jessie-backports openjdk-8-jre-headless ca-
certificates-java && \  
apt-get install -yqq --no-install-recommends git bzip2 curl unzip && \  
npm install -g gulp bower && \  
npm cache clean && \  
apt-get -yqq autoremove && \  
apt-get -yqq clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*  
  
# Allow root for bower  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Download sonar  
RUN curl --insecure -OL https://sonarsource.bintray.com/Distribution/sonar-
scanner-cli/${SONAR_SCANNER_PACKAGE} && \  
unzip ${SONAR_SCANNER_PACKAGE} -d /home && \  
rm ${SONAR_SCANNER_PACKAGE}  

