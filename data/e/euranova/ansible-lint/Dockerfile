FROM williamyeh/ansible:ubuntu16.04  
  
RUN apt-get update && \  
apt-get install -y git python-pip && \  
rm -rf /var/lib/apt/lists/*  
RUN pip install --upgrade pip && \  
pip install ansible==2.3.1.0 && \  
pip install ansible-lint==3.4.13  

