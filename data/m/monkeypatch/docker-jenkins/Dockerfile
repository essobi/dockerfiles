FROM jenkins:latest  
  
# Install plugins from the plugins.txt file  
COPY plugins.txt /usr/share/jenkins/  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
  
# Switch to root user to change folder owner  
USER root  
RUN chown -hR jenkins /var/jenkins_home  
RUN chown -hR jenkins /opt  
RUN apt-get update && \  
apt-get install -y nodejs nodejs-legacy npm && \  
apt-get autoremove  
# RUN usermod -a -G root jenkins  
# Set upgrade state  
RUN echo 2.0 > /usr/share/jenkins/jenkins.install.UpgradeWizard.state  
  
# Set mail from (https://wiki.jenkins-
ci.org/display/JENKINS/Features+controlled+by+system+properties)  
ENV JAVA_OPTS -Dmail.from=tools@monkeypatch.io
-Dhudson.footerURL=http://www.monkeypatch.io  
  
# Restore user jenkins  
USER jenkins  

