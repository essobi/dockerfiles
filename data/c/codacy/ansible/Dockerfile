FROM codacy/base  
  
# Install ansible  
  
RUN apt-get -y update && \  
apt-get -y install build-essential checkinstall && \  
apt-get -y install libgmp3-dev && \  
apt-get -y install python python-dev libffi-dev libssl-dev && \  
wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python && \  
rm -rf setuptools*.zip && \  
sudo easy_install pip && \  
pip install pip --upgrade --upgrade --ignore-installed --no-cache-dir && \  
pip install ansible==1.9.2 \--upgrade --ignore-installed --no-cache-dir && \  
apt-get -y install libsystemd-journal0 apparmor libsystemd-id128-0
libdevmapper1.02.1 && \  
ln -s /lib/x86_64-linux-gnu/libdevmapper.so.1.02.1 /lib/x86_64-linux-
gnu/libdevmapper.so.1.02 && \  
sudo rm -rf ~/.pip/cache && \  
sudo rm -rf /root/.pip/cache && \  
apt-get -y clean && \  
apt-get -y autoclean && \  
apt-get -y autoremove && \  
apt-get purge -y $(apt-cache search '~c' | awk '{ print $2 }') && \  
sudo rm -rf /tmp/ansible && \  
sudo rm -rf /var/lib/apt/lists/* && \  
sudo rm -rf /var/cache/apt && \  
sudo rm -rf /var/cache/oracle-jdk8-installer && \  
sudo rm -rf /tmp/*  

