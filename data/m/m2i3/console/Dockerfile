#  
# simple console for managing content of running containers with utilities  
# typical usage  
# docker run -t -i -volumes-from existing-container m2i3/console  
# where existing-container is a container on your system  
#  
FROM ubuntu:trusty  
MAINTAINER Jean-Marc Lagace <jean-marc@m2i3.com>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y wget unzip nano less lsb-release git
curl rsync  
  
CMD ["/bin/bash","--login"]  
  

