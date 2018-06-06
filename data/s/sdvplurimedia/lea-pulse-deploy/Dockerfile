FROM node:9.8.0  
# Before starting, needing apt-transport-https  
RUN apt-get update && apt-get install -y apt-transport-https  
  
# Sources update + installation for : jq, apt-transport-https, openssh-client  
RUN apt-get update && apt-get install -y jq ca-certificates openssh-client
rsync  
  
# Verify that we have all our tools installed to finish the build  
RUN which curl  
RUN which jq  
RUN which ssh-add  
RUN which rsync  
RUN which yarn  

