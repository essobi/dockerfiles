# Image: pitchplay/jenkins-volume  
# Version: 1.0.0  
FROM python:3-onbuild  
MAINTAINER Evan Lowry <evan@pitchplay.io>  
  
# Initial Setup  
RUN mkdir -p /var/jenkins_home/plugins  
RUN chown -R 1000:1000 /var/jenkins_home  
  
# Get Plugins  
RUN python genplugins.py  
RUN mv *.hpi /var/jenkins_home/plugins/  
  
# Cleanup  
RUN rm -rf /usr/src/app/*  
  
VOLUME ["/var/jenkins_home"]  
CMD ["true"]  

