FROM debian:stretch  
MAINTAINER Guillaume Gérard "guillaume.gerard88@gmail.com"  
# These dictate where to install devkitPro/A64 and dictate where they are
found  
# in project makefiles.  
ENV DEVKITPRO /opt/devkitPro  
ENV DEVKITA64 $DEVKITPRO/devkitA64  
  
# It allows to run commands manually  
ENV PATH $DEVKITA64/bin:$PATH  
  
RUN apt-get update && \  
apt-get install -y \  
bzip2 \  
xz-utils \  
make \  
perl \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget
https://raw.githubusercontent.com/devkitPro/installer/master/perl/devkitA64update.pl
-O devkitA64update.pl && \  
perl devkitA64update.pl && \  
rm devkitA64update.pl *.tar.bz2  
  
RUN mkdir /source  
WORKDIR /source  
CMD ["bash"]  

