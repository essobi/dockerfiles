FROM google/cloud-sdk  
MAINTAINER Peter Wiggers <peter@bitlayer.nl>  
  
# install pip  
RUN apt-get update && apt-get install -y python-pip git  
  
# install sops  
RUN curl -LO
https://github.com/mozilla/sops/releases/download/3.0.3/sops_3.0.3_amd64.deb
&& \  
dpkg -i sops_3.0.3_amd64.deb  
  
# install requirements  
COPY requirements.txt /tmp  
RUN pip install --no-cache-dir -r /tmp/requirements.txt  

