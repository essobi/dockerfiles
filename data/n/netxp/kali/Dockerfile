FROM kalilinux/kali  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "deb http://http.kali.org/kali sana main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali sana main contrib non-free" >>
/etc/apt/sources.list && \  
echo "deb http://security.kali.org/kali-security sana/updates main contrib
non-free" >> /etc/apt/sources.list && \  
echo "deb-src http://security.kali.org/kali-security sana/updates main contrib
non-free" >> /etc/apt/sources.list && \  
apt-get -yqq update && apt-get install -f && \  
apt-get -yqq --force-yes install openssh-server && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/list/*  
CMD ["/usr/sbin/sshd", "-D"]  
  

