FROM java:8  
WORKDIR /tmp  
  
ADD https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.6.1.zip sonar-scanner-2.6.1.zip  
RUN unzip sonar-scanner-2.6.1.zip && \  
rm sonar-scanner-2.6.1.zip && \  
mv sonar-scanner-2.6.1 /sonar-scanner  
  
RUN mkdir -p /opt/code  
WORKDIR /opt/code  
  
ENTRYPOINT /sonar-scanner/bin/sonar-scanner  
CMD -Dsonar.projectBaseDir=/opt/code  

