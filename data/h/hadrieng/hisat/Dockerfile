FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install hisat2  
RUN wget
ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.5-Linux_x86_64.zip
&& \  
unzip hisat2-2.0.5-Linux_x86_64.zip  
  
# add hisat to path  
ENV PATH /hisat2-2.0.5:$PATH  
  
# install samtools  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar xf samtools-1.3.1.tar.bz2 && \  
cd samtools-1.3.1 && \  
make && \  
make install && \  
cd .. && \  
rm -rf samtools-1.3.1  
  
# install stringtie  
RUN wget
http://ccb.jhu.edu/software/stringtie/dl/stringtie-1.3.1c.Linux_x86_64.tar.gz
&& \  
tar xzf stringtie-1.3.1c.Linux_x86_64.tar.gz  
  
# add stringtie to path  
ENV PATH /stringtie-1.3.1c.Linux_x86_64:$PATH  

