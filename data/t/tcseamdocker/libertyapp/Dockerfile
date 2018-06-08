# Base image and maintainer details  
FROM tcseamdocker/libertyserver  
MAINTAINER Enterprise AppsMaker masterCraft.support@tcs.com  
USER root  
# Copy config files  
COPY Deployment/InitW1/InstallationComponent/appserver/server.xml
/opt/ibm/wlp/usr/servers/defaultServer  
COPY Deployment/InitW1/InstallationComponent/scripts/startservers.sh /home  
RUN chmod 777 /home/startservers.sh  
# Expose the http, database and administration ports  
EXPOSE 8080 9443  
# Specify container startup command  
CMD /home/startservers.sh

