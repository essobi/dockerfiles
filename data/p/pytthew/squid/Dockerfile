FROM debian  
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y squid squidclient net-tools tcpdump telnet htop \  
&& ln -sf /usr/share/zoneinfo/Europe/Budapest /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get clean && rm -rf /var/lib/apt/lists/  
ADD squid /etc/init.d/squid  
RUN chmod 755 /etc/init.d/squid  
ENTRYPOINT ["/etc/init.d/squid","start"]  

