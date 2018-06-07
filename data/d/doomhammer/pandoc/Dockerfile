FROM debian  
MAINTAINER Piotr Gaczkowski <DoomHammerNG@gmail.com>  
  
RUN apt-get update && \  
apt-get install -qqy \  
libgmp10 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD
https://github.com/jgm/pandoc/releases/download/1.15/pandoc-1.15-1-amd64.deb
/src/pandoc-1.15.1-amd64.deb  
  
RUN dpkg -i /src/pandoc-1.15.1-amd64.deb && rm -rf /src  
  
ENTRYPOINT [ "/usr/bin/pandoc" ]  

