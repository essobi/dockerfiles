FROM kalilinux/kali-linux-docker  
MAINTAINER boogy "linuxhackk@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install metasploit  
RUN grep "kali-rolling main contrib non-free" /etc/apt/sources.list \  
|| echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list  
  
RUN apt-get -y update ; \  
apt-get -y upgrade; \  
apt-get -y dist-upgrade ; \  
apt-get -y install \  
ruby \  
metasploit-framework \  
tmux \  
vim  
  
RUN mkdir -p /templates \  
&& wget https://live.sysinternals.com/psfile.exe -O /templates/psfile.exe \  
&& wget https://live.sysinternals.com/psfile64.exe -O /templates/psfile64.exe
\  
&& wget https://live.sysinternals.com/procexp.exe -O /templates/procexp.exe \  
&& wget https://live.sysinternals.com/procexp64.exe -O
/templates/procexp64.exe  
  
ADD ./run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD ["start_msf"]  

