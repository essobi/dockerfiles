FROM python:2.7  
  
RUN apt-get update -q && \  
apt-get install -qy rsync jq && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p ~/downloads && \  
wget -P ~/downloads -c -nv
https://packages.chef.io/files/stable/chefdk/2.3.4/debian/7/chefdk_2.3.4-1_amd64.deb
&& \  
dpkg -i ~/downloads/chefdk_2.3.4-1_amd64.deb && \  
rm ~/downloads/chefdk_*.deb && \  
pip install --no-cache-dir Fabric==1.13.1  

