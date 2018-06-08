FROM python:2.7  
MAINTAINER nasuno@ascade.co.jp  
  
WORKDIR /tmp  
ADD
http://depot.galaxyproject.org/package/linux/x86_64/tophat/tophat-2.0.9.Linux_x86_64.tar.gz
tophat-2.0.9.Linux_x86_64.tar.gz  
ADD
http://depot.galaxyproject.org/package/linux/x86_64/bowtie2/bowtie2-2.1.0-linux-x86_64.tgz
bowtie2-2.1.0-linux-x86_64.tgz  
ADD
http://depot.galaxyproject.org/package/linux/x86_64/samtools/samtools-0.1.18-linux-x86_64.tgz
samtools-0.1.18-linux-x86_64.tgz  
  
RUN tar zxf tophat-2.0.9.Linux_x86_64.tar.gz  
RUN tar zxf bowtie2-2.1.0-linux-x86_64.tgz  
RUN tar zxf samtools-0.1.18-linux-x86_64.tgz  
  
RUN cp -R samtools-0.1.18/* /usr/local/  
RUN cp bowtie2-2.1.0/bowtie2* /usr/local/bin/  
RUN cp tophat-2.0.9.Linux_x86_64/* /usr/local/bin/  
  
RUN rm -rf tophat* bowtie2* samtools*  

