FROM jenkinsci/jenkins:2.73.3  
MAINTAINER Nick Griffin, <nicholas.griffin>  
  
ENV GERRIT_HOST_NAME gerrit  
ENV GERRIT_PORT 8080  
ENV GERRIT_SSH_PORT 29418  
ENV GERRIT_PROFILE="ADOP Gerrit" GERRIT_JENKINS_USERNAME=""
GERRIT_JENKINS_PASSWORD=""  
# Copy in configuration files  
COPY resources/plugins.txt /usr/share/jenkins/ref/  
COPY resources/init.groovy.d/ /usr/share/jenkins/ref/init.groovy.d/  
COPY resources/scripts/ /usr/share/jenkins/ref/adop_scripts/  
COPY resources/jobs/ /usr/share/jenkins/ref/jobs/  
COPY resources/scriptler/ /usr/share/jenkins/ref/scriptler/scripts/  
COPY resources/views/ /usr/share/jenkins/ref/init.groovy.d/  
COPY resources/m2/ /usr/share/jenkins/ref/.m2  
COPY resources/entrypoint.sh /entrypoint.sh  
COPY resources/scriptApproval.xml /usr/share/jenkins/ref/  
  
# Reprotect  
USER root  
RUN chmod +x -R /usr/share/jenkins/ref/adop_scripts/ && chmod +x
/entrypoint.sh  
# USER jenkins  
# 2.73.3 changes compliance  
## SSHD Module 2.0 has been integrated towards the Jenkins 2.69 release  
RUN echo " KexAlgorithms diffie-hellman-group1-sha1,diffie-hellman-group-
exchange-sha256" >> /etc/ssh/ssh_config  
  
# Pre-requisites  
RUN apt-get update && apt-get install -y zip ldap-utils python-pip telnet
netcat net-tools strace && rm -rf /var/lib/apt/lists/*  
  
# Environment variables  
ENV ADOP_LDAP_ENABLED=true ADOP_ACL_ENABLED=true ADOP_SONAR_ENABLED=true
ADOP_ANT_ENABLED=true ADOP_MAVEN_ENABLED=true ADOP_NODEJS_ENABLED=true
ADOP_GERRIT_ENABLED=true  
ENV LDAP_GROUP_NAME_ADMIN=""  
ENV JENKINS_OPTS="--prefix=/jenkins -Djenkins.install.runSetupWizard=false"  
ENV
PLUGGABLE_SCM_PROVIDER_PROPERTIES_PATH="/var/jenkins_home/userContent/datastore/pluggable/scm"  
ENV
PLUGGABLE_SCM_PROVIDER_PATH="/var/jenkins_home/userContent/job_dsl_additional_classpath/"  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  
  
ENTRYPOINT ["/entrypoint.sh"]  

