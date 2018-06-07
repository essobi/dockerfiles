FROM node  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
libasound2 \  
libgconf2-4 \  
libgtk2.0-0 \  
libnss3 \  
libx11-xcb1 \  
libxtst6 \  
libxss1 \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
# To be shared with source build image  
#RUN \  
# npm install -g yarn && \  
# npm install -g aulisius/jira-task-helper  

