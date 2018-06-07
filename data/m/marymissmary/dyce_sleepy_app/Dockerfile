## Setting up data container with sleepy app info  
FROM tianon/true  
  
##  
## The DyCE container expects the following directory structure:  
##  
## For an application's scripts and configuration files:  
## /dyce/dyce/<app name>  
##  
## For an application's web pages:  
## /dyce/apps/<app name>  
##  
#  
COPY dyce/dyce /usr/local/dyce/dyce  
VOLUME /usr/local/dyce/dyce  
  
COPY dyce/apps /usr/local/dyce/apps  
VOLUME /usr/local/dyce/apps  
  
CMD ["/true"]  

