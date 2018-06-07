FROM kalilinux/kali-linux-docker  
MAINTAINER Adam Ossenford <AdamOssenford@gmail.com>  
RUN apt-get install wordlists john -y && gunzip
/usr/share/wordlists/rockyou.txt.gz  
ENTRYPOINT ["/usr/sbin/john"]  

