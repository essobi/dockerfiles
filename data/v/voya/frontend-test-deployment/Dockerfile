FROM ubuntu:16.04  
# update  
RUN apt-get update -qqy  
RUN apt-get install -y curl wget software-properties-common git  
RUN add-apt-repository ppa:openjdk-r/ppa  
  
# install Node  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
# install Java  
RUN apt-get install -y default-jre openjdk-7-jre  
  
# allow more file system watchers, prevent ENOSPC --
https://github.com/facebook/jest/issues/3254  
RUN echo fs.inotify.max_user_watches=524288 | tee -a /etc/sysctl.conf &&
sysctl -p  
  
# install test & deployment dependencies  
RUN npm install --quiet -g @deployjs/cli bower protractor  
  
WORKDIR /opt/atlassian/bitbucketci/agent/build  

