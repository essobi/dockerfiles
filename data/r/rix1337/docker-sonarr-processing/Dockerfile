FROM linuxserver/sonarr  
MAINTAINER rix1337  
  
# Install Requirements  
RUN apt-get update && apt-get install -y mkvtoolnix  
  
# add local files  
COPY root/ /  
  
RUN chmod +x /processing/processing.sh  

