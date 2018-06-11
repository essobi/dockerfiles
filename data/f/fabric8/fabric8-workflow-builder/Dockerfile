FROM rawlingsj/fabric8-jenkins:latest  
  
MAINTAINER fabric8.io <fabric8@googlegroups.com>  
  
# Unfortunately for now we have to run as root so that we can use the docker
commands  
USER root  
  
ADD builder.sh /opt/builder.sh  
WORKDIR /opt  
CMD bash '/opt/builder.sh';  

