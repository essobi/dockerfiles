FROM python:2.7  
MAINTAINER John Pfeiffer "https://github.org/johnpfeiffer"  
# https://cloud.google.com/sdk/docs/quickstart-linux  
ENV VERSION 156.0.0  
RUN curl --silent https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-
key add -  
RUN apt-get update && \  
apt-get install -y lsb-release  
  
# https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu  
RUN export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \  
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a
/etc/apt/sources.list.d/google-cloud-sdk.list  
RUN apt-get update && \  
apt-get install -y google-cloud-sdk  
  
# https://golang.org/dl/  
# https://github.com/docker-
library/golang/blob/64b88dc3e9d83e71eafc000fed1f0d5e289b3e65/1.8/Dockerfile  
ENV GOVERSION 1.8.3  
RUN wget --quiet https://storage.googleapis.com/golang/go${GOVERSION}.linux-
amd64.tar.gz && \  
tar -C /usr/local -xzf go${GOVERSION}.linux-amd64.tar.gz && \  
rm go${GOVERSION}.linux-amd64.tar.gz  
ENV GOROOT /usr/local/go  
ENV PATH=$PATH:$GOROOT/bin  
ENV GOPATH /root  
RUN gcloud --version && \  
go version  
  

