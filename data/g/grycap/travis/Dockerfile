FROM ubuntu:16.04  
MAINTAINER alpegon3@upv.es  
  
# Update and install all the necessary packages  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
software-properties-common \  
sudo \  
iproute2 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc \  
&& rm -rf /usr/share/man  
  
# Install Ansible.  
RUN apt-add-repository -y ppa:ansible/ansible \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ansible \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc \  
&& rm -rf /usr/share/man  
  
# Install Ansible inventory file  
RUN printf '%s\n' '[local]' 'localhost ansible_connection=local' >
/etc/ansible/hosts  

