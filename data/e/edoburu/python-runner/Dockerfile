# Extra package for projects that need to run `ansible` as well.  
#  
# This image layer adds some additional packages needed for our deploys,  
# and by building on top of the existing python-runner the layer size stays
small.  
# For a clean pure ansible package see:
https://hub.docker.com/r/weldpua2008/docker-ansible/  
#  
# TO build: docker build -t edoburu/python-runner:ansible .  
#  
# We use `dig` for `{{ lookup('pipe', 'dig +short ' ~ carbon_server ~ ' A')`  
# so that needs to be present as well. ssh is available for the transport
support.  
  
FROM edoburu/python-runner:base  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends openssh-client dnsutils && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /var/cache/debconf/*-old && \  
pip install --no-cache-dir 'ansible<2.0' httplib2  

