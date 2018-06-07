FROM jenkinsci/jenkins:latest  
  
# RUN /usr/local/bin/install-plugins.sh git  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN xargs /usr/local/bin/install-plugins.sh <
/usr/share/jenkins/ref/plugins.txt  
  
ENV JENKINS_USER admin  
ENV JENKINS_PASS admin  
  
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false  
  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/

