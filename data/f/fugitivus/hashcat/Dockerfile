#hashcat container for teaching password security improvement:  
FROM fugitivus/debian:latest  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#environment-variables for non-interactive shell:  
#ENV DEBIAN_FRONTEND noninteractive  
  
#install some packages to build hashcat:  
RUN apt-get update && apt-get install\  
m4 lzip git make wget gcc libgmp3-dev libc6-dev-i386 -y\  
&& git clone https://github.com/hashcat/hashcat-legacy.git\  
  
#build hashcat and gmp:  
&& cd /hashcat-legacy\  
&& wget -c https://gmplib.org/download/gmp/gmp-6.1.0.tar.lz\  
&& cd /hashcat-legacy && tar xfv gmp-6.1.0.tar.lz\  
&& cd /hashcat-legacy/gmp-6.1.0\  
&& ./configure --host=i386-pc-linux-gnu\  
\--prefix=/hashcat-legacy/deps/gmp/linux32 --disable-shared\  
&& make install\  
&& cd /hashcat-legacy\  
&& make linux\  
&& cp hashcat-cli64.bin /sbin/hashcat\  
&& cp hashcat-cli32.bin /sbin/hashcat32\  
  
#do some cleanup:  
&& apt-get remove --purge -y git make gcc wget\  
m4 libc6-dev-i386 lzip\  
&& apt-get clean autoclean\  
&& apt-get autoremove -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/\  
&& cd / && rm -r hashcat-legacy  
  

