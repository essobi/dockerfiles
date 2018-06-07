FROM ubuntu:16.04  
  
COPY ./requirements.txt /requirements.txt  
  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
python-pip libssl-dev docker.io git wget unzip virtualbox \  
; \  
rm -rf /var/lib/apt/lists/* ; \  
wget https://releases.hashicorp.com/vagrant/2.0.4/vagrant_2.0.4_x86_64.deb &&
\  
dpkg -i vagrant_2.0.4_x86_64.deb && \  
rm vagrant_2.0.4_x86_64.deb && \  
ln -s /usr/bin/vagrant /bin/vagrant && \  
vagrant plugin install vagrant-openstack-provider ; \  
wget https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip
&& \  
unzip -q packer_1.2.3_linux_amd64.zip && \  
rm packer_1.2.3_linux_amd64.zip && \  
mv packer /bin/ ; \  
pip install --no-cache-dir -r /requirements.txt  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

