FROM python:2.7  
MAINTAINER Novemberde "novemberde.github.io"  
RUN apt-get update && \  
apt-get --no-install-recommends install -q -y openjdk-7-jre-headless && \  
apt-get install -y build-essential && \  
rm -rf /var/lib/apt/lists/*  
ADD http://mirrors.jenkins-ci.org/war/2.20/jenkins.war /opt/jenkins.war  
  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
  
EXPOSE 8080  
VOLUME /jenkins  
  
CMD [""]

