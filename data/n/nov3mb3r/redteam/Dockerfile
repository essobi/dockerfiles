FROM kalilinux/kali-linux-docker  
  
ENV SUDO_USER root  
  
RUN apt update && \  
apt install -y kali-linux-top10 \  
nikto \  
wpscan \  
sqlmap \  
sqlninja \  
scapy \  
set && \  
wget downloads.skullsecurity.org/passwords/rockyou.txt.bz2 && \  
bzip2 -d rockyou.txt.bz2  
  
  
  

