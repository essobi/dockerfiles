FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y curl python3 python3-requests python3-yaml  
  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
mv kubectl /usr/bin && \  
chmod +x /usr/bin/kubectl  
  

