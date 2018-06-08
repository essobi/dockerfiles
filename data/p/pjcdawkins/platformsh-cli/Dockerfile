FROM php:7-cli  
  
RUN apt-get update  
  
# Install Git and SSH CLI clients.  
RUN apt-get install --no-install-recommends -y git ssh-client  
  
# Install the Platform.sh CLI  
ADD install-cli.sh .  
RUN bash ./install-cli.sh  

