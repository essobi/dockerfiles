FROM ubuntu:wily  
RUN apt-get -y update \  
&& apt-get -y install --no-install-recommends \  
vim \  
git \  
nano \  
wget \  
curl \  
ca-certificates \  
net-tools \  
&& apt-get -y clean all \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.2.0/bin/linux/amd64/kubectl /usr/local/bin/kubectl  
ADD https://get.docker.com/builds/Linux/x86_64/docker-1.9.0
/usr/local/bin/docker  
ADD https://github.com/docker/compose/releases/download/1.6.0-rc1/docker-
compose-Linux-x86_64 /usr/local/bin/docker-compose  
ADD https://github.com/nds-
org/ndslabs/releases/download/v1.0.1-alpha/ndslabsctl-linux-amd64
/usr/local/bin/ndslabsctl  
COPY FILES.system-shell /  
RUN chmod a+x /usr/local/bin/*  
  
RUN echo '. ${HOME}/.bashrc-nds-sys' >> /root/.bashrc  
  
CMD usage  

