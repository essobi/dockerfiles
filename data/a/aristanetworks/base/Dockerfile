# Copyright (c) 2017 Arista Networks, Inc. All rights reserved.  
# Arista Networks, Inc. Confidential and Proprietary.  
FROM ubuntu:16.04  
LABEL maintainer="Fabrice Rabaute fabrice@arista.com"  
  
# Environment variables  
ENV USER prod  
ENV HOME /home/${USER}  
  
# Install various tools  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
at \  
ca-certificates \  
curl \  
iproute \  
iputils-ping \  
less \  
netcat \  
net-tools \  
software-properties-common \  
strace \  
tcpdump \  
unzip \  
vim \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod u+s /bin/ping  
  
# Install dumb-init  
RUN wget -nv https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 -O /usr/bin/dumb-init \  
&& echo "81231da1cd074fdc81af62789fead8641ef3f24b6b07366a1c34e5b059faf363
/usr/bin/dumb-init" \  
| sha256sum --strict --check - \  
&& chmod +x /usr/bin/dumb-init  
  
# Create the user and move into $HOME  
RUN useradd -m ${USER} -u 1000  
WORKDIR ${HOME}  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  

