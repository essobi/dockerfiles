FROM microsoft/dotnet:core-deps  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
unzip  
## SETUP CONSUL  
ADD /consul /var/consul  
  
RUN mkdir /var/consul/config  
  
RUN ls -l /var/consul  
  
RUN ip -o -4 addr list  
  
RUN chmod -R 777 /var/consul  
  
RUN wget
https://releases.hashicorp.com/consul/1.1.0/consul_1.1.0_linux_amd64.zip --no-
check-certificate  
  
RUN unzip consul_1.1.0_linux_amd64.zip -d /var/consul  
  
# Server RPC is used for communication between Consul clients and servers for
internal  
# request forwarding.  
EXPOSE 8300  
# Serf LAN and WAN (WAN is used only by Consul servers) are used for gossip
between  
# Consul agents. LAN is within the datacenter and WAN is between just the
Consul  
# servers in all datacenters.  
EXPOSE 8301 8301/udp 8302 8302/udp  
  
# CLI, HTTP, and DNS (both TCP and UDP) are the primary interfaces that
applications  
# use to interact with Consul.  
EXPOSE 8400 8500 8600 8600/udp  
  
### SETUP Zeus  
RUN wget https://github.com/Elders/Zeus/releases/download/1.1.0/zeus-
debian.8-x64.zip --no-check-certificate  
  
RUN unzip zeus-debian.8-x64.zip -d /var/zeus  
  
RUN ls /var/zeus  
  
RUN chmod -R 777 /var/zeus  
  
WORKDIR /var/  
  
ENTRYPOINT ["bash","./consul/entrypoint.sh"]  
##ENTRYPOINT ["/var/app/Zeus"]  

