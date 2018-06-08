FROM python:2.7  
MAINTAINER nasuno@ascade.co.jp  
  
ADD
https://github.com/samtools/samtools/releases/download/1.2/samtools-1.2.tar.bz2
samtools-1.2.tar.bz2  
RUN tar jxf samtools-1.2.tar.bz2  
RUN cd samtools-1.2 && make && mv samtools /usr/local/bin/  
RUN rm -rf samtools-1.2*  

