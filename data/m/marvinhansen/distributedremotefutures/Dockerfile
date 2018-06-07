############################################################  
# Dockerfile to build incremental DRF container images from base image  
############################################################  
  
  
FROM distributedremotefutures/dev-base:latest  
  
# File Author / Maintainer  
MAINTAINER Marvin Hansen <marvin.hansen@gmail.com>  
  
  
#Update the image  
RUN apt-get update  
RUN apt-get upgrade -y  
  
  
RUN cd /home/dev/DistributedRemoteFutures  
  
  
# update the local repo  
CMD [git pull]  
  
# Whatever SBT action would be useful....  
CMD [sbt compile]  
  
  
################## SAMPLE ######################  
# Here could be the command to execute when the container starts i.e.  
#CMD ["/usr/local/bin/StartScript.sh"]  
#  
# For a node-docker, a simpler way woud be  
# 1) wget http://www.mymirror.com/myJar  
# 2) EXPOSE 9090  
# 3) CMD [java -Jar myJar]  
# if a script is required, just stuff everying in a zip, use wget, unzip &
chmod before execution.  
#  
################## SAMPLE END ###################  

