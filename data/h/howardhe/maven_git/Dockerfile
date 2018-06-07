FROM java:8  
  
MAINTAINER Howard He "howard.he0329@gmail.com"  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget curl git maven  
  
VOLUME /volume/git  
RUN mkdir -p /local/git  
WORKDIR /local/git  
  
CMD ["/bin/bash"]

