# Provides NCBI BLAST+ binaries, mainly for use with Galaxy Project dockerised
runners  
  
FROM debian:wheezy  
  
MAINTAINER Simon Belluzzo <simon@belluzzo.id.au>  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
curl \  
python-minimal=2.7.3-4+deb7u1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /opt/blast \  
&& curl ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.30/ncbi-
blast-2.2.30+-x64-linux.tar.gz \  
| tar -zxC /opt/blast \--strip-components=1  
  
ENV PATH /opt/blast/bin:$PATH  

