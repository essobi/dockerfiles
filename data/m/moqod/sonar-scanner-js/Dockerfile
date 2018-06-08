from openjdk:jre-slim  
ENV SONAR_SCANNER_VERSION 3.0.3.778  
RUN apt update && apt install -y wget gnupg apt-utils  
RUN wget https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip\  
&& unzip sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip\  
&& rm sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip\  
&& mv /sonar-scanner-${SONAR_SCANNER_VERSION}-linux /sonar-scanner  
RUN apt-get install -y curl && curl -sL https://deb.nodesource.com/setup_7.x |
bash - && apt-get install -y nodejs && curl -L
https://www.npmjs.com/install.sh | sh  
RUN mkdir /code  
VOLUME /code  
WORKDIR /code  
ENTRYPOINT ["/sonar-scanner/bin/sonar-scanner"]  

