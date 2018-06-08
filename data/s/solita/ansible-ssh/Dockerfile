FROM solita/ubuntu-systemd-ssh:16.04  
  
RUN apt-get update && \  
apt-get install -y \  
python-setuptools \  
python-dev \  
gcc \  
libffi-dev \  
libssl-dev \  
git  
RUN easy_install pip  
RUN pip install ansible==2.1.0.0  
  
RUN useradd -m ansible -s /bin/bash  
RUN mkdir /home/ansible/.ssh && \  
touch /home/ansible/.ssh/authorized_keys && \  
chmod 700 /home/ansible/.ssh && \  
chmod 600 /home/ansible/.ssh/authorized_keys &&\  
chown -R ansible:ansible /home/ansible/.ssh  

