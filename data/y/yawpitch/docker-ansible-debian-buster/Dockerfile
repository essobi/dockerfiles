FROM debian:buster  
LABEL maintainer="Michael Morehouse (yawpitch)"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
sudo \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Install Ansible dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential libffi-dev libssl-dev python-pip python-dev \  
zlib1g-dev libncurses5-dev systemd python-setuptools python-wheel \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Install Ansible via pip  
RUN pip install ansible  
  
# Install Ansible inventory file.  
COPY hosts /etc/ansible/hosts  
  
# Restore initctl.  
COPY initctl_faker .  
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  
  
# Clean up.  
RUN apt-get clean && apt-get autoclean -y && apt-get autoremove -y  
  
# Set initial cmd  
CMD ["/bin/systemd"]  

