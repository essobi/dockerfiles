FROM ubuntu  
MAINTAINER scortum  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install bash && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  
  

