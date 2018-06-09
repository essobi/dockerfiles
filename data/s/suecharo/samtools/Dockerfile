# Docker image for Samtools  
FROM ubuntu:trusty  
MAINTAINER suecharo, suehiro619@gmail.com  
  
# Install build tools  
RUN apt-get update && apt-get install -y \  
wget \  
make \  
gcc \  
libncurses-dev \  
zlib1g-dev \  
libbz2-dev \  
liblzma-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Samtools  
WORKDIR /src  
RUN wget
https://sourceforge.net/projects/samtools/files/samtools/1.6/samtools-1.6.tar.bz2
\  
&& tar -jxvf samtools-1.6.tar.bz2 \  
&& rm -rf samtools-1.6.tar.bz2 \  
&& cd samtools-1.6 \  
&& ./configure \  
&& make \  
&& make install  
  
WORKDIR /mount  
CMD ["bash"]  

