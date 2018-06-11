# Base image and maintainer details  
FROM tcseamdocker/weblogic1036  
MAINTAINER Enterprise AppsMaker masterCraft.support@tcs.com  
USER root  
COPY Deployment/InitW1/InstallationComponent/scripts/startservers.sh /home  
COPY Deployment/InitW1/InstallationComponent/scripts/myDomain-ds.properties
/home/wls/base_domain  
# Create necessary directories and set permissions  
ADD Deployment/InitW1/InstallationComponent/runtimeconfig/ConfigDir
/home/ConfigDir  
RUN chmod 555 /home/startservers.sh && \  
chmod 777 /home/ConfigDir  
# Expose the http, database and administration ports  
EXPOSE 7001  
# Specify container startup command  
CMD bash ./home/startservers.sh

