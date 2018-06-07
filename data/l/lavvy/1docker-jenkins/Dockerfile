FROM debian:jessie  
MAINTAINER Allan Espinosa "allan.espinosa@outlook.com"  
RUN apt-get update && \  
apt-get --no-install-recommends install -q -y openjdk-7-jre-headless && \  
rm -rf /var/lib/apt/lists/*  
ADD http://mirrors.jenkins-ci.org/war/1.625/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
#added chroot support  
RUN ln -sf /bin/true /usr/bin/ischroot &&\  
ln -sf /bin/true /sbin/initctl  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]  

