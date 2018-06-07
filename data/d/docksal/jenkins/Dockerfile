FROM jenkins:2.7.4-alpine  
  
USER root  
  
# Skip initial setup.  
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false" \  
# Customizable settings:  
# Default admin user.  
JENKINS_USER=admin \  
JENKINS_PASS=admin \  
# Default email.  
JENKINS_EMAIL=admin@localhost \  
# Default URL.  
# This is necessary because Jenkins cannot reliably detect such a URL from
within itself.  
JENKINS_URL=http://192.168.64.100:8080/  
  
COPY jenkins.sh /usr/local/bin/jenkins.sh  
RUN chmod +x /usr/local/bin/jenkins.sh  
  
# Get plugins list.  
COPY plugins.txt /tmp/  
# Add initial YADP configuration.  
COPY configs/config.xml /usr/share/jenkins/default-config/  
# Custom JENKINS groovy scripts...  
COPY groovy/*.groovy /usr/share/jenkins/ref/init.groovy.d/  
  
# Install plugins from txt file.  
RUN /usr/local/bin/install-plugins.sh $(cat /tmp/plugins.txt | tr '\n' ' ')  
  
# Exposed ports.  
EXPOSE 50000-50100  
EXPOSE 80  
EXPOSE 8080  

