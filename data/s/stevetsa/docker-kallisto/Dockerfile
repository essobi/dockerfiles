####  
# Kallisto - kallisto is a program for quantifying abundances of transcripts
from RNA-Seq data  
# Nicolas L Bray, Harold Pimentel, Páll Melsted and Lior Pachter, Near-optimal
probabilistic RNA-seq quantification  
# Nature Biotechnology 34, 525–527 (2016), doi:10.1038/nbt.3519  
####  
FROM ubuntu:latest  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
MAINTAINER Steve Tsang <mylagimail2004@yahoo.com>  
RUN apt-get update  
  
RUN apt-get install --yes \  
build-essential \  
gcc-multilib \  
apt-utils \  
zlib1g-dev \  
cmake \  
libhdf5-dev  
  
RUN apt-get install -y wget  
RUN apt-get install -y git-all  
  
#RUN echo $HOME ### /root  
#RUN pwd  
# Get latest source from releases  
WORKDIR /  
RUN git clone https://github.com/pachterlab/kallisto.git  
#RUN tar xvzf kallisto_linux-v0.43.1.tar.gz  
WORKDIR kallisto  
RUN mkdir build  
WORKDIR build  
RUN pwd  
RUN cmake ..  
RUN make  
RUN make install  
  
# Add paths  
ENV PATH $HOME/bin:$PATH  
ENV LD_LIBRARY_PATH $HOME/lib/:$LD_LIBRARY_PATH  

