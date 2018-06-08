FROM node:6.11.5  
## install and configure dependencies  
ADD bootstrap.sh /usr/local/bin/bootstrap  
RUN chmod +x /usr/local/bin/bootstrap  
RUN bootstrap  
  
## set up script for pipelines to deploy results to build server  
ADD deploy.sh /usr/local/bin/deploy  
RUN chmod +x /usr/local/bin/deploy  
  
## set up script for pipelines to bump version number  
ADD bump_version.sh /usr/local/bin/bump_version  
RUN chmod +x /usr/local/bin/bump_version  
  
## set up script for pipelines to update build status after version bump  
ADD update_status.sh /usr/local/bin/update_status  
RUN chmod +x /usr/local/bin/update_status  

