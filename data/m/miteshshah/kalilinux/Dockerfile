FROM officialkali/kali  
MAINTAINER Mr.Miteshah@gmail.com  
  
RUN echo "deb http://http.kali.org/kali sana main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali sana main contrib non-free" >>
/etc/apt/sources.list && \  
echo "deb http://security.kali.org/kali-security sana/updates main contrib
non-free" >> /etc/apt/sources.list && \  
echo "deb-src http://security.kali.org/kali-security sana/updates main contrib
non-free" >> /etc/apt/sources.list  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update Packages  
RUN apt-get -y update && apt-get -y dist-upgrade  
  
# Install Kali Linux Web Metapackage  
RUN apt-get -y install kali-linux-web  
RUN apt-get -y install kali-linux-top10 && apt-get clean  
  
# Fix Metaspoit DB Issue  
RUN msfdb init  
  
# Fix Webspoit Module Issue  
RUN apt-get -y install python-scapy  
  
# Set root user password  
RUN echo 'root:toor' | chpasswd  
  
# Allow root user ssh  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
CMD ["/bin/bash"]  

