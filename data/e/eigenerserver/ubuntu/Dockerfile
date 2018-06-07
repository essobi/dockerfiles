FROM ubuntu:16.04  
  
LABEL description="Hedgehog Cloud by www.eigener-server.ch
https://www.eigener-server.ch/en/igel-cloud \  
is licensed under a Creative Commons Attribution 4.0 International Lizenz \  
http://creativecommons.org/licenses/by/4.0/ \  
To remove the links visit https://www.eigener-server.ch/en/igel-cloud"  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install net-tools tzdata && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# Disable SSH  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Timezone  
ENV TZ Europe/Zurich  
RUN echo ${TZ} >/etc/timezone && \  
ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# Fix Let's Encrypt CA not included in Ubuntu's CA bundle  
RUN apt-get update && \  
apt-get -y --no-install-recommends install --reinstall ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

