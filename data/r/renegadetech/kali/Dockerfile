FROM phusion/baseimage:0.9.22  
WORKDIR /home/root  
  
RUN gpg --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6 && \  
gpg -a --export ED444FF07D8D0BF6 | apt-key add - && \  
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list && \  
printf 'Dpkg::Options {\n"--force-confdef";\n "--force-confold";\n }\n' >
/etc/apt/apt.conf.d/local && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
locale-gen "en_US.UTF-8"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENTRYPOINT ["/sbin/my_init"]  
CMD ["/bin/bash", "--", "-l"]  

