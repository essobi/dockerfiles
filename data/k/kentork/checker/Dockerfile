FROM ubuntu:16.04  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends git curl wget httpie tree jq
netcat iputils-ping iproute2 dnsutils unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

