FROM iwsaas/jenkins  
MAINTAINER Henry Huang <henry.s.huang@gmail.com>  
  
ENV JENKINS_HOME /var/jenkins_home  
USER root  
COPY config.xml $JENKINS_HOME/  
COPY credentials.xml $JENKINS_HOME/  
RUN mkdir -p $JENKINS_HOME/jobs/ami-builder  
COPY job.xml $JENKINS_HOME/jobs/ami-builder/config.xml  
ENTRYPOINT ["/usr/local/bin/jenkins.sh"]  

