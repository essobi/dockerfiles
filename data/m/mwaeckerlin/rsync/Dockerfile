FROM mwaeckerlin/ubuntu  
MAINTAINER mwaeckerlin  
  
RUN apt-get install -y rsync  
  
ENTRYPOINT ["/usr/bin/rsync", "-avP", "--delete"]  

