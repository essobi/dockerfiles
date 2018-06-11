FROM debian:testing  
MAINTAINER Michal Belica <devel@beli.sk>  
EXPOSE 22  
# install packages  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
bind9-host \  
bind9utils \  
curl \  
iptables \  
netcat \  
nmap \  
openssh-server \  
tcpdump \  
wget \  
ca-certificates \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# prepare sshd  
RUN mkdir /var/run/sshd \  
&& sed -ri 's/^#?PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN curl -L -o /usr/local/bin/kubectl
https://storage.googleapis.com/kubernetes-release/release/$(curl -s
https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && chmod 0755
/usr/local/bin/kubectl  
COPY entrypoint /entrypoint  
  
CMD ["/bin/bash", "/entrypoint"]  

