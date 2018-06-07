FROM sonarqube:6.1-alpine  
  
RUN apk --update add \  
git \  
curl \  
tmux \  
htop && \  
apk del build-base && \  
rm -rf /var/cache/apk/*  
  
ENV TZ=Europe/Lisbon  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
ADD https://sonarsource.bintray.com/Distribution/sonar-php-plugin/sonar-php-
plugin-2.9.0.1664.jar "/opt/sonarqube/extensions/plugins"  
ADD https://sonarsource.bintray.com/Distribution/sonar-github-plugin/sonar-
github-plugin-1.3.jar "/opt/sonarqube/extensions/plugins"  
  
ENV SONAR_SCANNER_VERSION=2.8  
ENV SONAR_SCANNER_HOME="/sonar-scanner"  
WORKDIR "/"  
  
RUN curl --insecure -OL \  
"https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-$SONAR_SCANNER_VERSION.zip"  
RUN unzip "/sonar-scanner-$SONAR_SCANNER_VERSION.zip" && \  
mv "sonar-scanner-$SONAR_SCANNER_VERSION" "sonar-scanner" && \  
rm "/sonar-scanner-$SONAR_SCANNER_VERSION.zip"  
  
ENV PATH=${PATH}:"$SONAR_SCANNER_HOME/bin"  
COPY sonar-scanner.properties "$SONAR_SCANNER_HOME/conf/sonar-
scanner.properties"  
  
WORKDIR "/opt/sonarqube/"  
  
COPY run.sh $SONARQUBE_HOME/bin/  
ENTRYPOINT ["./bin/run.sh"]  
  

