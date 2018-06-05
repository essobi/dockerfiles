FROM ubuntu:16.04  
  
COPY start.sh /a/start.sh  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt update \  
&& apt install -y wget perl \  
&& wget -O - https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add
- \  
&& echo "deb http://build.openvpn.net/debian/openvpn/release/2.4 xenial main"
> /etc/apt/sources.list.d/openvpn-aptrepo.list \  
&& apt update \  
&& apt install -y openvpn ssmtp iptables p7zip-full whois \  
&& wget -qO- "https://github.com/OpenVPN/easy-
rsa/releases/download/v3.0.4/EasyRSA-3.0.4.tgz" \  
| tar -xzC /tmp \  
&& mv /tmp/EasyRSA* /etc/openvpn/easy-rsa \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& chmod +x /a/start.sh  
  
CMD /a/start.sh

