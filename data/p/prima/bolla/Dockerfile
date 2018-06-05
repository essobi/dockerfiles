FROM prima/elixir-official:1.6.5  
MAINTAINER Andrea Usuelli <andrea.usuelli@prima.it>  
  
RUN apt-get update && \  
apt-get install -f -qqy \  
curl \  
tar \  
gzip \  
vim \  
mysql-client \  
postgresql-client-9.6 \  
python2.7 python-pip && \  
pip install awscli && \  
rm -r /var/lib/apt/lists/* && \  
aws configure set default.s3.signature_version s3v4 && \  
aws configure set default.region eu-west-1 && \  
curl -s -L -o ./biscuit-linux_amd64.tgz
https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-
linux_amd64.tgz && \  
tar xzvf biscuit-linux_amd64.tgz && \  
mv biscuit /usr/bin/biscuit && \  
chmod +x /usr/bin/biscuit && \  
rm biscuit-linux_amd64.tgz  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

