FROM fedora  
  
RUN dnf install -y which net-tools make gcc less curl binutils  
RUN curl -L -o /tmp/softether.tar.gz http://www.softether-
download.com/files/softether/v4.25-9656-rtm-2018.01.15-tree/Linux/SoftEther_VPN_Server/64bit_-
_Intel_x64_or_AMD64/softether-
vpnserver-v4.25-9656-rtm-2018.01.15-linux-x64-64bit.tar.gz && tar xzf
/tmp/softether.tar.gz -C /opt && cd /opt/vpnserver && echo -e "1\n1\n1\n" |
make  
  
COPY files/start.sh /opt/start.sh  
RUN chmod 755 /opt/*.sh  
  
ENTRYPOINT /opt/start.sh  
  

