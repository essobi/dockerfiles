FROM gitlab/dind  
MAINTAINER Hugo Briand <briand@ekino.com>  
  
RUN apt-get update -q && \  
apt-get install -qy \  
build-essential \  
python-pip \  
groff-base && \  
pip install awscli && \  
  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/*  

