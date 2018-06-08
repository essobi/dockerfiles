# escape=`  
ARG VERSION=latest  
FROM jenkins:$VERSION AS jenkins  
  
WORKDIR /var/jenkins_home  
USER root  
RUN apt-get update && apt-get install git -y  
RUN mkdir -p /var/jenkins_home/init.groovy.d && chown jenkins:jenkins
/var/jenkins_home/init.groovy.d  
USER jenkins  
HEALTHCHECK \--interval=5m --timeout=3s CMD curl -f
http://localhost:8080/status/ || exit 1  
  
COPY init.groovy.d /var/jenkins_home/init.groovy.d  

