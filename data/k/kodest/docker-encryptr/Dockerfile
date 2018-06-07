FROM debian:latest  
MAINTAINER Laszlo ASHIN <laszlo.ashin@mailfence.com>  
ADD
https://spideroak.com/dist/encryptr/signed/linux/deb/encryptr_2.0.0-1_amd64.deb
/tmp/  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libasound2 \  
libfontconfig1 \  
libgconf-2-4 \  
libglib2.0-0 \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libpangocairo-1.0-0 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxi6 \  
libxrandr2 \  
libxtst6 \  
&& dpkg -i /tmp/encryptr_*.deb \  
&& rm /tmp/encryptr_*.deb  
ENTRYPOINT [ "/usr/bin/Encryptr" ]  

