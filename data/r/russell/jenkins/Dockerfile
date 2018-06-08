FROM stackbrew/ubuntu:14.04  
MAINTAINER Russell Clare "Russell@Clare.io"  
RUN apt-get update && apt-get clean  
RUN apt-get install -q -y openjdk-7-jre-headless && apt-get clean  
ADD http://mirrors.jenkins-ci.org/war/latest/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war", "--prefix=/jenkins"]  
EXPOSE 8080  
CMD [""]  

