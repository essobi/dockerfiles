FROM openjdk:8-alpine  
  
RUN apk add --no-cache curl grep sed unzip  
  
# Set timezone to CST  
ENV TZ=Europe/Rome  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
WORKDIR /root  
  
RUN curl --insecure -o ./sonarscanner.zip -L
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.0.3.778-linux.zip  
RUN unzip sonarscanner.zip  
RUN rm sonarscanner.zip  
  
WORKDIR /  
  
ENV SONAR_RUNNER_HOME=/root/sonar-scanner-3.0.3.778-linux  
ENV PATH $PATH:/root/sonar-scanner-3.0.3.778-linux/bin  
  
# ensure Sonar uses the provided Java for musl instead of a borked glibc one  
RUN sed -i 's/use_embedded_jre=true/use_embedded_jre=false/g' /root/sonar-
scanner-3.0.3.778-linux/bin/sonar-scanner  

