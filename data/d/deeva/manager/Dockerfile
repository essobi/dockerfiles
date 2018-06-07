FROM ubuntu:latest  
MAINTAINER Anthony Powles  
  
CMD ["/bin/bash", "-l"]  
  
ENV LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
GO_VERSION=1.6 \  
GLIDE_VERSION=0.10.2 \  
GOROOT=/opt/go  
ENV PATH=$GOROOT/bin:$PATH  
  
RUN groupadd deeva \  
&& useradd -m -s /bin/bash -g deeva deeva  
  
RUN locale-gen en_US.UTF-8 \  
&& apt-get update -y \  
&& apt-get install -qy --no-install-recommends \  
ca-certificates \  
curl \  
git \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -s https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz | tar -C /opt -zx \  
&& mkdir /opt/glide \  
&& curl -sL
https://github.com/Masterminds/glide/releases/download/${GLIDE_VERSION}/glide-${GLIDE_VERSION}-linux-
amd64.tar.gz | tar -C /opt/glide -zx \  
&& ln -s /opt/glide/linux-amd64/glide /usr/local/bin/glide  
  
USER deeva  
  

