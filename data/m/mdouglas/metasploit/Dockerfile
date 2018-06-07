FROM phusion/baseimage:0.9.19  
ENV metasploit_package=metasploit-
framework_4.13.3%2B20161129103013~1rapid7-1_amd64.deb  
  
RUN apt-get update -y \  
&& apt-get install -y curl nmap \  
&& rm -rf /var/lib/apt/lists/*  
RUN curl https://apt.metasploit.com/pool/main/m/metasploit-
framework/${metasploit_package} > /tmp/metasploit.dpkg \  
&& dpkg -i /tmp/metasploit.dpkg \  
&& rm /tmp/metasploit.dpkg \  
&& apt-get purge -y --auto-remove curl  
  
VOLUME ["/root/.msf4"]  
  
CMD ["/usr/bin/msfconsole"]

