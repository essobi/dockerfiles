FROM java:jre-alpine  
  
RUN apk add --update python py-pip  
RUN pip install -U setuptools  
RUN pip install -U pylint  
  
ADD https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-cli-3.0.3.778.zip ./package.zip  
  
RUN unzip package.zip && mv ./sonar-scanner* ./sonar-scanner  
  
ADD entrypoint.sh .  
RUN chmod +x /entrypoint.sh  
  
ENV SONAR_SCANNER_OPTS="-Xmx512m"  
ENV SONAR_SOURCES="."  
WORKDIR /src  
ENTRYPOINT [ "/entrypoint.sh" ]

