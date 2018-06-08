FROM ubuntu:16.04  
  
# Install golang  
RUN apt-get update -y && \  
apt-get install -y curl && \  
curl -O https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz && \  
tar -xvf go1.8.linux-amd64.tar.gz && \  
mv go /usr/local  
  
# Install Docker  
RUN apt-get update -y && \  
apt-get install -y linux-image-extra-4.11.0-14-generic linux-image-extra-
virtual apt-transport-https ca-certificates software-properties-common && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- && \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable" && \  
apt-get update -y && \  
apt-get install -y docker-ce  
  
ENV PATH=$PATH:/usr/local/go/bin  
  
ENV GOROOT=/usr/local/go  
ENV PATH=$PATH:$GOROOT/bin

