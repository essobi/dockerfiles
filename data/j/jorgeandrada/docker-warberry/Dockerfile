FROM debian:latest  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Docker DocToc" \  
org.label-schema.description="Generates table of contents for markdown files
inside local git repository." \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/doctoc" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run --rm -it jorgeandrada/docker-warberry"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir -p /root/warberry/Tools/Responder \  
&& mkdir -p /root/warberry/Results \  
&& mkdir -p /root/warberry/warberry \  
&& sed -i 's/main/main contrib non-free/g' /etc/apt/sources.list \  
&& apt-get update && apt-get install -y \  
wget \  
nbtscan \  
python-pip \  
python-scapy \  
tcpdump \  
nmap \  
python-nmap \  
python-bluez \  
smbclient \  
samba \  
samba-common-bin \  
unzip \  
python-dev \  
python3-dev \  
ppp \  
xprobe2 \  
sg3-utils \  
netdiscover \  
macchanger \  
libpcap-dev \  
onesixtyone \  
nikto \  
hydra \  
john \  
bridge-utils \  
w3af-console \  
ettercap-text-only \  
cryptcat \  
git \  
ike-scan \  
&& pip install optparse-pretty \  
netaddr \  
ipaddress \  
subprocess32 \  
pypcap \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN git clone https://github.com/DanMcInerney/net-creds.git
/root/warberry/Tools/net-creds \  
&& git clone https://github.com/sqlmapproject/sqlmap.git
/root/warberry/Tools/sqlmap \  
&& git clone https://github.com/CoreSecurity/impacket.git
/root/warberry/Tools/impacket \  
&& git clone https://github.com/samratashok/nishang.git
/root/warberry/Tools/nishang \  
&& git clone https://github.com/SpiderLabs/Responder.git
/root/warberry/Tools/Responder \  
&& git clone https://github.com/PowerShellMafia/PowerSploit.git
/root/warberry/Tools/PowerSploit \  
&& git clone https://github.com/offensive-security/exploit-database.git
/root/warberry/Tools/exploit-database \  
&& git clone https://github.com/secgroundzero/warberry.git /usr/src/warberry \  
&& cp -r /usr/src/warberry/* /root/warberry/warberry \  
&& rgrep -l "sudo" /root/warberry/warberry | xargs sed -i 's/sudo//g'  
  
RUN update-ca-certificates \  
&& wget --no-check-certificate http://seclists.org/nmap-
dev/2016/q2/att-201/clamav-exec.nse -O /usr/share/nmap/scripts/clamav-exec.nse
\  
&& wget --no-check-certificate
https://labs.portcullis.co.uk/download/enum4linux-0.8.9.tar.gz -P /tmp/ \  
&& tar -zxvf /tmp/enum4linux-0.8.9.tar.gz -C /root/warberry/Tools/ \  
&& mv /root/warberry/Tools/enum4linux-0.8.9 /root/warberry/Tools/enum4linux \  
&& wget https://download.sysinternals.com/files/SysinternalsSuite.zip -P
/root/warberry/Tools/ \  
&& unzip /root/warberry/Tools/SysinternalsSuite.zip -d
/root/warberry/Tools/sysinternals/ \  
&& rm /root/warberry/Tools/SysinternalsSuite.zip \  
&& rm -rf /tmp/*  
  
WORKDIR /root/warberry  
  
CMD ["python","/root/warberry/warberry/warberry.py"]  

