FROM python:3  
RUN \  
apt-get update && \  
apt-get install -yqq apt-transport-https zip  
RUN \  
echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list && \  
wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- && \  
apt-get update && \  
apt-get install -yqq nodejs && \  
pip install boto3==1.3.0 # required for lambda_deploy.py && \  
rm -rf /var/lib/apt/lists/*

