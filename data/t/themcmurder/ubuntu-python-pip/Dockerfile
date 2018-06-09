FROM ubuntu:wily  
MAINTAINER Justin McMurdie <mcmurdiej@gmail.com>  
  
ENV HOME /root  
  
RUN apt-get update && \  
apt-get install -y git curl sudo && \  
apt-get install -y build-essential python python-pip libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/bin/bash", "--login", "-i", "-c"]  
CMD ["/bin/bash"]  

