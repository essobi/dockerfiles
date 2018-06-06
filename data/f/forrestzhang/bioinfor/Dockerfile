FROM forrestzhang/ubuntu-dev  
  
MAINTAINER Tao Zhang "forrestzhang1982@gmail.com"  
RUN apt-get update && apt-get install -y samtools  
  
RUN mkdir /opt/software  
  
#picard 2.2.2, tophat 2.1.1, cufflinks 2.2.1, bowtie2 2.2.6, sratoolkit  
ADD https://github.com/broadinstitute/picard/releases/download/2.2.2/picard-
tools-2.2.2.zip /opt/software/  
ADD
https://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.1.Linux_x86_64.tar.gz
/opt/software/  
ADD http://cole-trapnell-
lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz
/opt/software/  
ADD
https://github.com/BenLangmead/bowtie2/releases/download/v2.2.6/bowtie2-2.2.6-linux-x86_64.zip
/opt/software/  
ADD http://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.6.2/sratoolkit.2.6.2-ubuntu64.tar.gz
/opt/software/  
  
WORKDIR /opt/software  
RUN unzip picard-tools-2.2.2.zip && mv picard-tools-2.2.2 picard  
RUN unzip bowtie2-2.2.6-linux-x86_64.zip && mv bowtie2-2.2.6 bowtie2  
RUN tar zxvf tophat-2.1.1.Linux_x86_64.tar.gz && mv tophat-2.1.1.Linux_x86_64
tophat  
RUN tar zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz && mv
cufflinks-2.2.1.Linux_x86_64 cufflinks  
RUN tar zxvf sratoolkit.2.6.2-ubuntu64.tar.gz && mv sratoolkit.2.6.2-ubuntu64
sratoolkit  
  
RUN git clone https://github.com/lh3/bwa.git && cd bwa && make  
  
ENV PATH
/opt/software/bowtie2:/opt/software/tophat:/opt/software/cufflinks:/opt/software/bwa:/opt/software/sratoolkit:$PATH  
ENV LANG en_US.UTF-8  

