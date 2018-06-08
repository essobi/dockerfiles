FROM java:8u45-jdk  
  
RUN apt-get update && apt-get install -y curl  
  
ENV JENKINS_HOME=/var/jenkins_home  
  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
  
RUN curl -fL http://mirrors.jenkins-ci.org/war-stable/1.609.1/jenkins.war -o
jenkins.war  
  
USER jenkins  
CMD java $JAVA_OPTS -jar /jenkins.war  
  
EXPOSE 8080  
EXPOSE 50000  

