#  
# This Dockerfile is used to create a bootstrap Jenkins image.  
#  
# It contains no specific Kadaster infrastructure dependencies. Infrastructure
dependencies are  
# added using an additional Dockerfile on top of this one that is maintained
within the Kadaster  
# premisis. This way, we keep the Kadaster infrastructure details secret.  
#  
# This image is built with the automated build facilities of
http://dockerhub.comn.  
#  
# Use the (latest if possible) LTS version of Jenkins  
FROM jenkins:2.19.1  
MAINTAINER SOO Support "soo@kadaster.nl"  
# Install all wanted plugins  
RUN /usr/local/bin/install-plugins.sh docker-commons \  
docker-plugin \  
github-organization-folder \  
greenballs \  
ldap \  
locale \  
nodejs \  
sonar \  
workflow-aggregator  
  
# Create the environment  
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"  
# Extra configuration files  
COPY ref/ /usr/share/jenkins/ref/  
  
# USER root  
# RUN chown -R jenkins:jenkins /usr/share/jenkins/ref  
# USER jenkins  

