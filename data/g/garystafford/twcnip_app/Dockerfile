# Apache Tomcat 8 image with customization for project:  
# https://github.com/garystafford/tw-cn-ip-build-deploy  
FROM tomcat:latest  
  
MAINTAINER Gary A. Stafford <garystafford@rochester.rr.com>  
  
LABEL version="1.1.1"  
  
RUN mv /usr/local/tomcat/webapps/ROOT /usr/local/tomcat/webapps/_ROOT  
  
COPY tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml  
COPY companyNews.war /usr/local/tomcat/webapps/ROOT.war

