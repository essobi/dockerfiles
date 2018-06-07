FROM lavaliere/jenkins-base  
  
MAINTAINER Tracy Kennedy  
  
# Download jenkins.war  
USER jenkins  
WORKDIR /usr/lib/jenkins  
RUN curl -L -O -w "Downloaded: %{url_effective}\\\n" "http://nectar-
downloads.cloudbees.com/nectar/latest/jenkins.war"  
  
EXPOSE 8080 22 9990 8888 443 33848  
ENV JENKINS_HOME /var/lib/jenkins  
  
USER root  
ENTRYPOINT ["java", "-jar", "jenkins.war", "--httpPort=8080"]  
CMD ["--prefix=/jenkins"]

