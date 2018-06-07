FROM brcomconcretesolutions/jenkins-security  
  
USER root  
  
# Loading jobs  
# Script that loads the Users from S3, your EC2 Role should have the
appropriate permissions  
COPY loadjobs.groovy /usr/share/jenkins/ref/init.groovy.d/loadjobs.groovy  
  
#setup the loadjobs and savejobs Jobs that integrate with S3  
COPY jobs /usr/share/jenkins/ref/jobs  
  
USER jenkins  

