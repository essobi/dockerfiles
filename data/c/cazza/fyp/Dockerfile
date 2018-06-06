FROM ubuntu:14.04  
RUN apt-get update && apt-get clean  
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean  
RUN apt-get install -y python python-dev python-distribute python-pip python-
pymongo  
ADD http://mirrors.jenkins-ci.org/war/1.601/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]  

