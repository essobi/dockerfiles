FROM ubuntu:14.04  
#MAINTAINER Kate Smith <ksmith@example.com>  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
libncurses-dev \  
unzip \  
zlib1g-dev  
  
RUN curl -L https://github.com/lh3/bwa/archive/v0.7.15.zip > /root/bwa.zip  
RUN unzip /root/bwa.zip -d /root  
RUN rm /root/bwa.zip  
#RUN sed -e's#INCLUDES=#INCLUDES=-I/root/zlib-1.2.8/ #'
-e's#-lz#/root/zlib-1.2.8/libz.a#' /root/bwa-0.7.15/Makefile >
/root/bwa-0.7.15/Makefile.zlib  
#RUN curl -L http://zlib.net/zlib-1.2.8.tar.gz > /root/zlib-1.2.8.tar.gz  
#RUN tar xvzf /root/zlib-1.2.8.tar.gz -C /root  
#RUN rm /root/zlib-1.2.8.tar.gz  
#RUN cd /root/zlib-1.2.8 && ./configure && cd ~/  
#RUN make -C /root/zlib-1.2.8  
#RUN make -C /root/bwa-0.7.15 -f Makefile.zlib  
RUN make -C /root/bwa-0.7.15  
RUN ln -s /root/bwa-0.7.15/bwa /usr/bin/bwa  
RUN curl -L https://github.com/samtools/htslib/archive/1.3.1.zip >
/root/htslib.zip  
RUN unzip /root/htslib.zip -d /root  
RUN rm /root/htslib.zip  
RUN make -C /root/htslib-1.3.1  
RUN curl -L https://github.com/samtools/samtools/archive/1.3.1.zip >
/root/samtools.zip  
RUN unzip /root/samtools.zip -d /root  
RUN rm /root/samtools.zip  
RUN make HTSDIR=/root/htslib-1.3.1 -C /root/samtools-1.3.1  
RUN ln -s /root/samtools-1.3.1/samtools /usr/bin/samtools  

