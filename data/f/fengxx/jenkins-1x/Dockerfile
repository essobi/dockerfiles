FROM jenkins:1.651.3  
# Create Jenkins Folder  
USER root  
RUN mkdir -p /var/lib/jenkins/jobs/mock_test  
RUN chown -R jenkins:jenkins /var/lib/jenkins  
  
USER jenkins  
ADD plugins.txt /tmp/  
ENV JENKINS_HOME /var/lib/jenkins  
RUN plugins.sh /tmp/plugins.txt  
COPY com.splunk.splunkjenkins.SplunkJenkinsInstallation.xml ${JENKINS_HOME}/  
COPY mock_job.xml ${JENKINS_HOME}/jobs/mock_test/config.xml  
VOLUME /var/lib/jenkins

