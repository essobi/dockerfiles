FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y \  
openssh-client \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/bin/bash"]  

