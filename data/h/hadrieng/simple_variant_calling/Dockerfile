FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
#installs samtools  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
tar xf samtools-1.3.1.tar.bz2 && \  
cd samtools-1.3.1 && \  
make && \  
make install && \  
cd .. && \  
rm -rf samtools-1.3.1  
  
#installs scythe  
RUN git clone https://github.com/vsbuffalo/scythe.git && \  
cd scythe && \  
make all && \  
cd ..  
  
#installs sickle  
RUN git clone https://github.com/najoshi/sickle.git && \  
cd sickle && \  
make && \  
cd ..  
  
#installs Bowtie2  
RUN wget https://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.2.9/bowtie2-2.2.9-linux-x86_64.zip && \  
unzip bowtie2-2.2.9-linux-x86_64.zip && \  
rm bowtie2-2.2.9-linux-x86_64.zip  
  
#adds scythe and sickle to the path  
ENV PATH /scythe:/sickle:/bowtie2-2.2.9:$PATH  

