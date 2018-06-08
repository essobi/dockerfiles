FROM ubuntu:16.04  
  
MAINTAINER Kevin Wilson <kevin.wilson@dc.gov>  
  
# Fix locales  
  
ENV LC_ALL=en_US.UTF-8  
ENV LANG=en_US.UTF-8  
  
RUN apt-get update && apt-get install -y locales && \  
sh -c 'echo "en_US.UTF-8 UTF-8" > /etc/locale.gen' && \  
locale-gen  
  
RUN apt-get update && \  
apt-get install -y software-properties-common vim && \  
add-apt-repository ppa:jonathonf/python-3.6 && \  
apt-get update && \  
apt-get install -y build-essential python3.6 python3.6-dev python3-pip
python3.6-venv && \  
apt-get install -y git && \  
rm -rf /var/lib/apt/lists/*  
  
RUN python3.6 -m pip install --upgrade pip wheel  

