FROM ubuntu:latest  
  
MAINTAINER "Kir Melnikov <kir@melniki.pro>"  
RUN apt-get update && apt-get install -y \  
curl \  
build-essential \  
libssl-dev \  
libffi-dev \  
git \  
golang-go \  
python-pip \  
python3 \  
python3-apt \  
python3-dev \  
python3-pip \  
npm \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip  
  
COPY requirements.txt /tmp/  
RUN pip install -r /tmp/requirements.txt  
RUN ansible --version && ansible-vault --version  

