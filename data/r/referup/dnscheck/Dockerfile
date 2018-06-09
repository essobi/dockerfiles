FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
dnsutils \  
curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
daemontools \  
inotify-tools \  
moreutils \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY cloe_run /usr/bin/cloe_run  
COPY dnscheck /usr/bin/dnscheck  
COPY users /dnscheck/users  
WORKDIR /dnscheck  
  
ENTRYPOINT [ "cloe_run", "${CLOE_RUN_BIN}" ]  

