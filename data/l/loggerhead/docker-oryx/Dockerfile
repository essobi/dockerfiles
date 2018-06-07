FROM loggerhead/docker-oryx:cdh5  
  
MAINTAINER loggerhead  
  
WORKDIR /tmp  
  
ADD scripts/ /tmp/  
ADD data/ /tmp/  
ADD oryx.conf /tmp/oryx.conf  
  
RUN apt-get update && apt-get install -y curl wget  
RUN /tmp/download-oryx.sh  

