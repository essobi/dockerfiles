FROM i386/ubuntu:devel  
MAINTAINER pevma "pmanev@oisf.net"  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common \  
software-properties-common net-tools iputils-ping man-db ethtool jq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:oisf/suricata-beta  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y suricata-dbg \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD service suricata start && bash  

