FROM williamyeh/ansible:ubuntu16.04  
RUN apt-get update && apt-get install -y \  
wget \  
iputils-ping \  
netcat-openbsd \  
corkscrew \  
git  
  
WORKDIR /etc/ansible  
  
CMD ["/bin/bash"]  

