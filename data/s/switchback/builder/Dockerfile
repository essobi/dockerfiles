FROM switchback/debian  
  
RUN apt-get update && \  
rm -rf /var/lib/apt/lists/*  
  
ENV BRANCH master  
ENV BUILD_NUMBER 0  
# create all the directories that we need  
RUN mkdir -p /var/default  
RUN mkdir -p /var/project  
RUN mkdir -p /var/workspace  
  
# defaults for client  
VOLUME /var/default  
# project directory  
VOLUME /var/project  
# workspace to do work  
VOLUME /var/workspace  

