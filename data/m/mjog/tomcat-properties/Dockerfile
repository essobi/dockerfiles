#  
# tomcat Dockerfile  
#  
# https://bitbucket.org/mjogltd/tomcat-properties  
#  
# Pull the official tomcat base image  
FROM tomcat:8.0-jre8  
  
# Remove the existing webapps directories  
RUN rm -rf /usr/local/tomcat/webapps/ROOT \  
&& rm -rf /usr/local/tomcat/webapps/docs \  
&& rm -rf /usr/local/tomcat/webapps/examples \  
&& rm -rf /usr/local/tomcat/webapps/host-manager \  
&& rm -rf /usr/local/tomcat/webapps/manager  
  
# Entrypoint script  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY env.awk /env.awk  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

