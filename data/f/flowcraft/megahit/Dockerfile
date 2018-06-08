FROM ubuntu:16.04  
MAINTAINER C I Mendes, cimendes@medicina.ulisboa.pt  
  
RUN apt-get update  
  
# -- General Dependencies ---  
RUN apt-get install -y wget python python3 zlib1g-dev build-essential  
  
# -- megahit ---  
RUN wget
https://github.com/voutcn/megahit/releases/download/v1.1.3/megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin.tar.gz  
RUN tar -xzf megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin.tar.gz && rm
megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin.tar.gz  
RUN mv megahit_v1.1.3_LINUX_CPUONLY_x86_64-bin megahit  
  
ENV PATH="/megahit/:$PATH"

