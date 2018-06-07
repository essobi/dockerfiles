FROM debian:stretch  
MAINTAINER Guillaume Gérard "guillaume.gerard88@gmail.com"  
# These dictate where to install devkitPro/ARM and dictate where they are
found  
# in project makefiles.  
ENV DEVKITPRO /opt/devkitPro  
ENV DEVKITARM $DEVKITPRO/devkitARM  
  
# It allows to run commands manually  
ENV PATH="${DEVKITARM}/bin:${PATH}"  
RUN apt-get update && \  
apt-get install -y \  
bzip2 \  
make \  
perl \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget
https://raw.githubusercontent.com/devkitPro/installer/master/perl/devkitARMupdate.pl
-O devkitARMupdate.pl && \  
perl devkitARMupdate.pl && \  
rm devkitARMupdate.pl *.tar.bz2  
  
RUN mkdir /source  
WORKDIR /source  
CMD ["bash"]  

