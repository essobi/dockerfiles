FROM debian:wheezy  
MAINTAINER Jeroen Geusebroek  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install dependencies.  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
sudo \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential libffi-dev libssl-dev python-pip python-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Upgrade the pip to lastest.  
RUN pip install -i https://pypi.python.org/simple/ -U pip && \  
ln -fs /usr/local/bin/pip /usr/bin/pip  
# Install Ansible via pip.  
RUN pip install ansible cryptography  
  
COPY initctl_faker .  
RUN chmod +x initctl_faker && rm -fr /sbin/initctl && ln -s /initctl_faker
/sbin/initctl  
  
# Install Ansible inventory file  
RUN mkdir -p /etc/ansible \  
&& echo "[local]\nlocalhost ansible_connection=local" > /etc/ansible/hosts  

