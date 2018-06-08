# Packer  
FROM debian:jessie  
MAINTAINER Kevin Littlejohn <kevin@littlejohn.id.au>  
  
# apt-get and cleanup  
RUN apt-get -yq update \  
&& apt-get -yq install curl ca-certificates build-essential git mercurial \  
sudo vim zlib1g-dev libssl-dev golang unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Environment variables in one hit  
ENV PATH=$PATH:/usr/local/packer \  
GOPATH=/usr/local/go \  
PYTHON_VER=2.7.9 \  
HOME=/home/packer  
  
RUN go get -u github.com/mitchellh/gox  
  
# Install packer  
RUN mkdir -p /usr/local/packer \  
&& cd /usr/local/packer \  
&& curl -O -L
https://releases.hashicorp.com/packer/0.8.6/packer_0.8.6_linux_amd64.zip \  
&& unzip packer_0.8.6_linux_amd64.zip \  
&& curl -O -L https://github.com/packer-community/packer-windows-
plugins/releases/download/v1.0.0/linux_amd64.zip \  
&& unzip -qo linux_amd64.zip  
  
# Run as a user for security friendliness  
RUN adduser --disabled-password --gecos "" packer; \  
echo "packer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
USER packer  
  
# Add my required config files  
WORKDIR /app  
  
# Suggested running: docker run -it -e AWS_SECRET_KEY -e AWS_  
ENTRYPOINT ["/usr/local/packer/packer"]  

