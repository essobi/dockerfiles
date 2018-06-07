FROM debian:jessie-slim  
  
MAINTAINER Heiko Holland  
  
LABEL Name=veracrypt  
LABEL Version=0.0.1  
  
WORKDIR /root  
  
RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y ntfs-3g wget bzip2 \  
&& apt-get clean all  
  
RUN wget
https://launchpad.net/veracrypt/trunk/1.21/+download/veracrypt-1.21-setup.tar.bz2
\  
&& tar -xjf veracrypt-1.21-setup.tar.bz2 \  
&& ./veracrypt-1.21-setup-console-x64 --noexec --target veracrypt \  
&& sed -i 's/TTY=0/TTY=1/g' ./veracrypt/veracrypt_install_console_x64.sh \  
&& sed -i 's/INSTALL=-1/INSTALL=1/g'
./veracrypt/veracrypt_install_console_x64.sh \  
&& sed -i 's/ACCEPTED=0/ACCEPTED=1/g'
./veracrypt/veracrypt_install_console_x64.sh \  
&& sed -i 's/$MORE/true/g' ./veracrypt/veracrypt_install_console_x64.sh \  
&& sed -i 's/&& read A//g' ./veracrypt/veracrypt_install_console_x64.sh \  
&& sed -i 's/read A//g' ./veracrypt/veracrypt_install_console_x64.sh \  
&& ./veracrypt/veracrypt_install_console_x64.sh \  
&& rm -rf veracrypt*  

