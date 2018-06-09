FROM openshift/origin  
  
ENV HOME /var/jenkins_home  
ENV JENKINS_HOME /var/jenkins_home  
  
RUN wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-
ci.org/redhat/jenkins.repo && \  
rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key && \  
yum install -y zip unzip java-1.7.0-openjdk docker jenkins && yum clean all  
  
RUN usermod -m -d "$JENKINS_HOME" jenkins && \  
chown -R jenkins "$JENKINS_HOME"  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
  
RUN pwd  
  
# for main web interface:  
EXPOSE 8080  
EXPOSE 50000  
USER jenkins  
  
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]

