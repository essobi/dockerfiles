FROM jenkinsci/jenkins:2.14  
COPY plugins.txt /plugins.txt  
RUN /usr/local/bin/plugins.sh /plugins.txt  
  
# Prevent the SetupWizard  
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
  
# Set master executors to 0  
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy  

