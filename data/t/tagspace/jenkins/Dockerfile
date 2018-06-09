FROM tagspace/java  
  
MAINTAINER Joshua Hansen <joshua@tagspace.com.au>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update dpkg  
RUN apt-get update  
  
# Install Git  
RUN apt-get install -y git  
  
# Install Jenkins  
ADD http://mirrors.jenkins-ci.org/war/latest/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
VOLUME /.jenkins  
ENV JENKINS_HOME /.jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]

