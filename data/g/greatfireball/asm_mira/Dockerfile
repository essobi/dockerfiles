FROM ubuntu:xenial  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de"  
LABEL description="Dockerfile providing the mira assembler"  
  
RUN apt update && apt install --yes wget bzip2  
  
RUN wget -O /tmp/mira.tar.bz2 https://sourceforge.net/projects/mira-
assembler/files/MIRA/stable/mira_4.0.2_linux-
gnu_x86_64_static.tar.bz2/download && cd /tmp/ && tar xjf mira.tar.bz2 && rm
mira.tar.bz2 && mv /tmp/mira* /opt/  
  
ENV PATH=/opt/mira_4.0.2_linux-gnu_x86_64_static/bin:$PATH  

