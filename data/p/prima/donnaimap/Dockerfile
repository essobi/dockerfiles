FROM golang:1.10.0  
  
RUN groupadd -g 1000 app && \  
useradd -g 1000 -u 1000 \--system \--create-home app && \  
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh && \  
apt-get update -q && \  
apt-get install -qy python-pip groff-base && \  
pip install awscli && \  
wget https://github.com/dcoker/biscuit/releases/download/v0.1.3/biscuit-
linux_amd64.tgz && \  
tar xzvf biscuit-linux_amd64.tgz && \  
mv biscuit /go/bin/biscuit && \  
chmod +x /go/bin/biscuit && \  
rm biscuit-linux_amd64.tgz && \  
aws configure set default.s3.signature_version s3v4 && \  
aws configure set default.region eu-west-1  
  
COPY files/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

