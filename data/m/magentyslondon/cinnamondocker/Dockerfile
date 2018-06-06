FROM jenkins/jenkins:lts  
USER root  
RUN apt-get update  
RUN apt-get install -y xvfb  
RUN apt-get install -y chromedriver  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install  
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/ref/plugins.txt
| tr -d '\r' | tr '\n' ' ')  
RUN mkdir -p /var/jenkins_home/jobs/Cinnamon-Demo/  
COPY job_config.xml /var/jenkins_home/jobs/Cinnamon-Demo/config.xml  
COPY org.jenkinsci.plugins.xvfb.Xvfb.xml /var/jenkins_home  
COPY jenkins.mvn.GlobalMavenConfig.xml /var/jenkins_home  
COPY hudson.tasks.Maven.xml /var/jenkins_home

