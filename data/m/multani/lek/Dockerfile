FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install \  
ca-certificates \  
curl \  
gcc \  
libffi-dev \  
libssl-dev \  
libyaml-dev \  
openssh-client \  
python-pip \  
python2.7 \  
python2.7-dev \  
rsync \  
\--yes \--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/* && \  
  
pip install \  
awscli==1.11.93 \  
Lektor==2.3  

