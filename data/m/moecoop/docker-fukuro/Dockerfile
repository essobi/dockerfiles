FROM dlanguage/dmd:latest  
MAINTAINER Mojo  
  
RUN apt-get update && \  
apt-get install -y git python3-pip libevent-dev && \  
pip3 install --upgrade pip && pip3 install mkdocs && \  
apt-get clean && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  

