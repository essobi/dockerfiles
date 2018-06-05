FROM java:openjdk-8-jre  
  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
# based on the work in docker definition of maluuba/tomcat7-java8  
# but starting from a specific java version docker image  
EXPOSE 8080  
# Required for apt-add-repository  
RUN apt-get update  
RUN apt-get install -y tomcat7  
RUN apt-get install -y tomcat7-admin  
RUN apt-get install -y logrotate  
# add bash for debugging abilities & support for custom scripts afterwards  
RUN apt-get install -y bash  
  
ADD config /config  
RUN chmod +x /config/*.sh  
  
RUN mv /etc/cron.daily/logrotate /etc/cron.hourly/logrotate  
RUN cp /config/logrotate /etc/logrotate.d/tomcat7  
RUN chmod 644 /etc/logrotate.d/tomcat7  
  
# make logs available under standard location  
RUN ln -s /var/log/tomcat7 /logs  
  
# add a volume which will contain all locally created files by the webapp  
# webapps should be configured to write into it.  
ADD data /data  
RUN chown -R tomcat7:tomcat7 /data  
RUN chmod 777 /data  
  
# use the build-in deployment support of tomcat to deploy a service  
# 1. create a context file in the contexts  
# 2. the webapps directory contains the war one likes to deploy  
ADD contexts /contexts  
ADD webapps /webapps  
  
ENTRYPOINT ["/config/startup-tomcat.sh"]  
  

