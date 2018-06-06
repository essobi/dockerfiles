FROM csrafaelpires/jenkins-awssdkruby  
  
USER root  
  
# Copying credentials  
# Script that loads the credentials from S3, your EC2 Role should have the
appropriate permissions  
COPY loadCredentials.groovy
/usr/share/jenkins/ref/init.groovy.d/loadCredentials.groovy  
  
#SMTP plugin configuration, check the environment variables  
COPY smtpconfig.groovy /usr/share/jenkins/ref/init.groovy.d/smtpconfig.groovy  
  
USER jenkins  
  
#setting up git plugin  
COPY gitplugin.txt /gitplugin.txt  
RUN plugins.sh gitplugin.txt

