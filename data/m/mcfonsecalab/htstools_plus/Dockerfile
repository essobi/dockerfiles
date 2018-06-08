FROM argrosso/htstools:0.1.2  
MAINTAINER Rui Luis <ruisergioluis@gmail.com>  
  
  
RUN apt-get update && apt-get install -y cmake git zlib1g-dev liblzo2-dev  
  
#bamtools v2.4.2  
RUN git clone git://github.com/pezmaster31/bamtools.git && \  
cd bamtools && mkdir build && cd build && cmake -DCMAKE_INSTALL_PREFIX=. .. &&
\  
make && make install && cp bin/bamtools /usr/local/bin && cd ../../ && rm -rf
bamtools  
  
#faToTwoBit  
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/faToTwoBit && \  
chmod +x faToTwoBit && mv faToTwoBit /usr/local/bin  
  
#rseqc v2.6.4  
RUN pip install RSeQC  
  
#Deeptools  
RUN pip install deeptools  
  
#Bedtools2 Update  
RUN rm -r bedtools2 && \  
git clone https://github.com/arq5x/bedtools2.git && \  
cd bedtools2 && \  
make && \  
make install  
  
#Samtools Update  
RUN wget
https://github.com/samtools/samtools/releases/download/1.7/samtools-1.7.tar.bz2
&& \  
tar -xjf samtools-1.7.tar.bz2 && \  
cd samtools-1.7 && \  
./configure --prefix=/usr/local/bin && \  
make && \  
make install  
  
#Multiqc  
RUN pip install multiqc  
  
#featureCounts Installation  
ARG PACKAGE_VERSION=1.6.1  
RUN wget -q
https://downloads.sourceforge.net/project/subread/subread-${PACKAGE_VERSION}/subread-${PACKAGE_VERSION}-source.tar.gz
&& \  
tar -xzf subread-${PACKAGE_VERSION}-source.tar.gz && \  
cd subread-${PACKAGE_VERSION}-source/src && \  
make -f Makefile.Linux && \  
cd ../bin && \  
mv utilities/* . && \  
rmdir utilities && \  
mv * /usr/local/bin/  
  
RUN apt-get remove git cmake -y  
RUN apt-get autoclean -y  

