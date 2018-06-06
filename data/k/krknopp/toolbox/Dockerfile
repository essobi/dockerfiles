FROM ubuntu:16.04  
RUN apt update && apt install -y \  
dnsutils \  
whois \  
git \  
vim \  
jq \  
python \  
python-pip \  
bsdmainutils \  
curl \  
wget  
  
RUN pip install --upgrade pip  
RUN pip install awscli  
  
RUN echo "set number" > /root/.vimrc  
  
CMD ["/bin/bash"]  

