FROM openjdk:8  
LABEL maintainer="Alekseii Erokhin <zmeffulka@gmail.com>"  
  
RUN apt-get update && apt-get install -y git curl bsdtar && rm -r
/var/cache/apt/archives/  
  
RUN curl --insecure -o /tmp/sonarscanner.zip -L
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.1.0.1141-linux.zip  
  
RUN mkdir /opt/sonar-scanner/ && cd /opt/sonar-scanner/ && bsdtar -xf
/tmp/sonarscanner.zip -s'|[^/]*/||' && rm /tmp/sonarscanner.zip  
  
ENV PATH $PATH:/opt/sonar-scanner/bin  
  
CMD /bin/bash  

