FROM java:openjdk-8-jre  
  
MAINTAINER Bert Van Nuffelen <bert.van.nuffelen@tenforce.com>  
# based on the work in docker definition of maluuba/tomcat7-java8  
# but starting from a specific java version docker image  
EXPOSE 8080  
# Required for apt-add-repository  
RUN apt-get update  
RUN apt-get install -y tomcat7 tomcat7-admin bash logrotate  
  
ADD startup-tomcat.sh /opt/startup-tomcat.sh  
RUN chmod +x /opt/startup-tomcat.sh  
  
RUN mv /etc/cron.daily/logrotate /etc/cron.hourly/logrotate  
  
ADD logrotate /etc/logrotate.d/tomcat7  
RUN chmod 644 /etc/logrotate.d/tomcat7  
  
ADD tomcat-setenv.sh /usr/share/tomcat7/bin/setenv.sh  
ADD tomcat-users.xml /var/lib/tomcat7/conf/tomcat-users.xml  
RUN chmod +x /usr/share/tomcat7/bin/setenv.sh  
RUN chown root:tomcat7 /var/lib/tomcat7/conf/tomcat-users.xml  
  
# use the build-in deployment support of tomcat to deploy a service  
# 1. create a context file in the contexts  
# 2. the webapps directory contains the war one likes to deploy  
#ADD unifiedviews.xml /etc/tomcat7/Catalina/localhost/unifiedviews.xml  
ADD contexts /contexts  
RUN mkdir -p /webapps  
  
ADD
http://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/master/3.0.0/master-3.0.0.war
/webapps/master-3.0.0.war  
ADD
http://repository.unifiedviews.eu/nexus/content/repositories/releases/eu/unifiedviews/frontend/3.0.0/frontend-3.0.0.war
/webapps/unifiedviews-3.0.0.war  
RUN chown -R tomcat7:tomcat7 /webapps  
  
ADD deployment /deployment  
  
ENTRYPOINT ["/opt/startup-tomcat.sh"]  
  

