#-------------------------------------------------------------------------------  
# Name: ngtrieuvi92/sonar-scanner  
# Description: Docker image to easy run sonar scanner  
# Usage:  
# docker run \  
# -v ./src:/data  
# -e SONAR_USERNAME="$SONAR_USERNAME" \  
# -e SONAR_PASSWORD="$SONAR_PASSWORD" \  
# ngtrieuvi92/sonar-scanner  
#  
#-------------------------------------------------------------------------------  
FROM java:alpine  
MAINTAINER vi.nt <vi.nt@geekup.vn>  
  
# Set scanner version  
ENV SONAR_SCANNER_VERSION 2.7  
# Install sonar scanner  
RUN apk add --no-cache wget && \  
wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-${SONAR_SCANNER_VERSION}.zip && \  
unzip sonar-scanner-${SONAR_SCANNER_VERSION} && \  
cd /usr/bin && ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-scanner
sonar-scanner && \  
apk del wget  
  
# Create /data directory and set as mount volume & workir  
RUN mkdir /data  
VOLUME /data  
WORKDIR /data  
  
CMD sonar-scanner -Dsonar.login=$SONAR_USERNAME
-Dsonar.password=$SONAR_PASSWORD  
  

