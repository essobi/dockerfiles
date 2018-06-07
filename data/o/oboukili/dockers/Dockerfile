FROM debian:jessie  
  
MAINTAINER boukili.olivier@gmail.com  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list  
RUN apt-get update -y && apt-get install --fix-missing && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
python python-yaml sudo curl gcc python-pip python-dev \  
python-requests libffi-dev libssl-dev git && \  
apt-get install -y -t jessie-backports jq && \  
apt-get -y \--purge remove python-cffi && \  
pip install --upgrade cffi  
RUN pip install ansible && \  
pip install ansible-lint && \  
pip install netaddr && \  
pip install scaleway_sdk && \  
pip install requests && \  
pip install pyhcl && \  
pip install python-consul && \  
pip install netaddr  
RUN apt-get -f -y \--auto-remove remove \  
gcc python-pip python-dev libffi-dev libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/*  
RUN mkdir -p /opt/ansible ~/.ssh && \  
chmod 755 ~/.ssh  
  
WORKDIR /opt/ansible  
CMD ["ansible-playbook"]  

