FROM whisk/jenkins:1.620  
COPY jenkins_plugins.txt /tmp/jenkins_plugins.txt  
RUN /usr/local/bin/plugins.sh /tmp/jenkins_plugins.txt  
COPY master-executors.groovy /usr/share/jenkins/ref/init.groovy.d/  

