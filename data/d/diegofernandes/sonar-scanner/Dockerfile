FROM circleci/openjdk:8-jdk  
## Based on this example http://stackoverflow.com/a/40612088/865222  
ENV SONAR_SCANNER_VERSION 3.0.3.778  
RUN sudo wget https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip && \  
sudo unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION} && \  
cd /usr/bin && sudo ln -s /sonar-scanner-${SONAR_SCANNER_VERSION}/bin/sonar-
scanner sonar-scanner  

