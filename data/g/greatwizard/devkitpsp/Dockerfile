FROM debian:stretch  
MAINTAINER Guillaume Gérard "guillaume.gerard88@gmail.com"  
# These dictate where to install devkitPro/PSP and dictate where they are
found  
# in project makefiles.  
ENV DEVKITPRO /opt/devkitPro  
ENV DEVKITPSP $DEVKITPRO/devkitPSP  
  
# It allows to run commands manually  
ENV PATH="${DEVKITPSP}/bin:${PATH}"  
RUN apt-get update && \  
apt-get install -y \  
bzip2 \  
make \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p $DEVKITPRO  
RUN wget
https://sourceforge.net/projects/devkitpro/files/devkitPSP/devkitPSP_r16-1-x86_64-linux.tar.bz2/download
-O devkitPSP.tar.bz2 && \  
tar xf devkitPSP.tar.bz2 -C $DEVKITPRO && \  
rm devkitPSP.tar.bz2  
  
RUN mkdir /source  
WORKDIR /source  
CMD ["bash"]  

