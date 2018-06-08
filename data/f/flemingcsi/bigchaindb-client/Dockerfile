FROM ubuntu:17.10  
LABEL maintainer="Jared Harrington-Gibbs"  
LABEL description="A docker image that can connect to bigchaindb instances."  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y python3.5 python3-pip
libffi-dev libssl-dev && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y vim iputils-ping net-tools
&& \  
pip3 install --upgrade setuptools && \  
pip3 install --upgrade pip && \  
pip3 install bigchaindb_driver && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
mkdir /scripts && \  
rm -rf /var/lib/apt/lists/*  
  
COPY scripts/ /scripts  
  
ENTRYPOINT ["bash"]  

