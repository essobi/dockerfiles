FROM ubuntu:xenial  
  
RUN apt-get update && \  
apt-get install -y \  
cpanminus \  
make \  
wget \  
bzip2 \  
git \  
gcc \  
zlib1g-dev  
  
WORKDIR /root  
  
RUN echo -e "y\no conf prerequisites_policy follow\no conf commit" | cpan && \  
cpanm File::Which && \  
cpanm Log::Log4perl  
  
RUN wget -O- ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-
blast-2.6.0+-x64-linux.tar.gz | tar zx && \  
cp ncbi-blast-2.6.0+/bin/* /usr/local/bin/ && \  
rm -fr /root/ncbi-blast-2.6.0+  
  
RUN wget -O samtools.tar.bz2
"https://downloads.sourceforge.net/project/biobin/xyztools/samtools-
only-1.4_x64-linux.tar.bz2?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fbiobin%2F%3Fsource%3Ddirectory&ts=1495099879&use_mirror=svwh"
&& \  
bunzip2 samtools.tar.bz2 && \  
tar -xvf samtools.tar && \  
cp samtools-only-1.4_x64-linux/samtools /usr/local/bin/ && \  
rm -fr /root/samtools-only-1.4_x64-linux && \  
rm -fr /root/samtools.tar  
  
RUN git clone https://github.com/BioInf-Wuerzburg/proovread && \  
cd proovread && \  
make PREFIX=/usr && \  
make install PREFIX=/usr && \  
cd /root && \  
rm -fr /root/proovread  
  
RUN apt-get autoremove -y git gcc bzip2 wget make && \  
apt-get autoremove -y  

