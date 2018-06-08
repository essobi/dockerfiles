FROM debian:7.6  
MAINTAINER David Vázquez <davazp@gmail.com>  
  
# Install dependencies from Debian repositories  
RUN apt-get update && apt-get install -y make wget bzip2 && apt-get clean  
  
# Install SBCL from the tarball binaries.  
RUN wget http://prdownloads.sourceforge.net/sbcl/sbcl-1.2.9-x86-64-linux-
binary.tar.bz2 -O /tmp/sbcl.tar.bz2 && \  
mkdir /tmp/sbcl && \  
tar jxvf /tmp/sbcl.tar.bz2 \--strip-components=1 -C /tmp/sbcl/ && \  
cd /tmp/sbcl && \  
sh install.sh && \  
cd /tmp \  
rm -rf /tmp/sbcl/  

