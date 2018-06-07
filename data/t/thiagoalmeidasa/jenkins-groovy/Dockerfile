FROM jenkinsci/jenkins:latest  
  
LABEL MAINTAINER "Thiago Almeida <thiago@mossteam.com.br>"  
  
RUN /usr/local/bin/install-plugins.sh workflow-aggregator job-dsl git build-
flow-plugin  
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false  
COPY admin.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY hello-dsl.groovy /usr/share/jenkins/ref/init.groovy.d/  
COPY fun-with-jenkins2.groovy /usr/share/jenkins/ref/init.groovy.d/  

