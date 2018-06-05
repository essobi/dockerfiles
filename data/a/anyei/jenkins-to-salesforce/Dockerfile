FROM jenkins:latest  
  
MAINTAINER anyei <angelyoelroblesmercedes@gmail.com>  
  
#Star me or leave any comment here: https://hub.docker.com/r/anyei/jenkins-to-
salesforce/  
#Please report issues here : https://github.com/anyei/jenkins-to-
salesforce/issues  
#Changing to root, it was running on jenkins user context  
USER root  
  
  
#INSTALLING GIT PLUGIN  
  
ADD http://updates.jenkins-ci.org/latest/parameterized-trigger.hpi
/usr/share/jenkins/ref/plugins/parameterized-trigger.hpi  
  
ADD http://updates.jenkins-ci.org/latest/mailer.hpi
/usr/share/jenkins/ref/plugins/mailer.hpi  
  
ADD http://updates.jenkins-ci.org/latest/token-macro.hpi
/usr/share/jenkins/ref/plugins/token-macro.hpi  
  
ADD http://updates.jenkins-ci.org/latest/scm-api.hpi
/usr/share/jenkins/ref/plugins/scm-api.hpi  
  
ADD http://updates.jenkins-ci.org/latest/promoted-builds.hpi
/usr/share/jenkins/ref/plugins/promoted-builds.hpi  
  
ADD http://updates.jenkins-ci.org/latest/git-client.hpi
/usr/share/jenkins/ref/plugins/git-client.hpi  
  
ADD http://updates.jenkins-ci.org/latest/git.hpi
/usr/share/jenkins/ref/plugins/git.hpi  
  
  
#INSTALLING ANT  
  
RUN mkdir -p /var/ant_home  
  
ADD http://ftp.wayne.edu/apache/ant/binaries/apache-ant-1.9.6-bin.zip
/var/ant_home/apache-ant-1.9.6-bin.zip  
  
RUN unzip /var/ant_home/apache-ant-1.9.6-bin.zip -d /var/ant_home && rm
/var/ant_home/apache-ant-1.9.6-bin.zip  
  
ENV ANT_HOME=/var/ant_home/apache-ant-1.9.6  
  
ENV PATH=${PATH}:${ANT_HOME}/bin  
  
#In case anyone is intersted, the following command would retreive additional
ant's plugins  
#RUN ant -f ${ANT_HOME}/fetch.xml -Ddest=sytem  
#INSTALLING SALESFORCE ANT PLUGIN  
RUN mkdir ${ANT_HOME}/lib/x  
  
ADD https://na17.salesforce.com/dwnld/SfdcAnt/salesforce_ant_34.0.zip
${ANT_HOME}/lib/x/salesforce_ant_34.0.zip  
  
RUN unzip ${ANT_HOME}/lib/x/salesforce_ant_34.0.zip -d ${ANT_HOME}/lib/x && cp
${ANT_HOME}/lib/x/ant-salesforce.jar ${ANT_HOME}/lib/ant-salesforce.jar && rm
-rf ${ANT_HOME}/lib/x  
  
RUN chown -R jenkins "${ANT_HOME}" "/usr/share/jenkins/ref/plugins"  
#Changing to jenkins user  
USER jenkins  

