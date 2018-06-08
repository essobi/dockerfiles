FROM golang:latest  
# Install inotify-tools to enable usage of inotifywait.  
RUN apt-get update  
RUN apt-get --yes --force-yes install inotify-tools  
ADD ./runreload.sh /runreload.sh  
# Ensure our script is executable.  
RUN chmod +x /runreload.sh  
ENTRYPOINT ["/runreload.sh"]  

