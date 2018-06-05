FROM ubuntu:16.04  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt update \  
&& apt install -y wget \  
&& wget --no-check-certificate -O - https://swupdate.openvpn.net/repos/repo-
public.gpg | apt-key add - \  
&& echo "deb http://build.openvpn.net/debian/openvpn/release/2.4 xenial main"
> /etc/apt/sources.list.d/openvpn-aptrepo.list \  
&& apt update \  
&& apt install -y openvpn \  
&& rm -rf /var/lib/apt/lists/*  

