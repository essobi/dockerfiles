FROM brcomconcretesolutions/jenkins-awscli  
  
USER root  
  
# Copying users  
# Script that loads the Users from S3, your EC2 Role should have the
appropriate permissions  
COPY enablesecurity.groovy
/usr/share/jenkins/ref/init.groovy.d/enablesecurity.groovy  
COPY loadCredentials.groovy
/usr/share/jenkins/ref/init.groovy.d/loadCredentials.groovy  
COPY smtpconfig.groovy /usr/share/jenkins/ref/init.groovy.d/smtpconfig.groovy  
  
USER jenkins  
  
#setting up role-strategy plugin  
COPY rolestrategyplugin.txt /rolestrategyplugin.txt  
RUN plugins.sh rolestrategyplugin.txt  

