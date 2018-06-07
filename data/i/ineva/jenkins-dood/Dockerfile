FROM jenkins:2.0-alpine  
  
USER root  
  
# copy docker command  
COPY docker /usr/bin/docker  
RUN chmod +x /usr/bin/docker  
  
# install theme: material-light  
COPY org.codefirst.SimpleThemeDecorator.xml
$JENKINS_HOME/org.codefirst.SimpleThemeDecorator.xml  
  
# install plugins  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

