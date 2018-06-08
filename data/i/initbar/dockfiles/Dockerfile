FROM ubuntu:17.10  
MAINTAINER Herbert Shin  
  
COPY . /src  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
lsb-release \  
sudo && \  
bash /src/docker/install.sh  
  
WORKDIR /root  
  
CMD ["/bin/bash"]  

