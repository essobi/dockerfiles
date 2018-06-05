FROM ubuntu:16.04  
MAINTAINER Danny Wells "danny@parkerici.org"  
RUN apt-get update \  
&& apt-get install -y software-properties-common wget \  
&& echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list \  
&& gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add - \  
&& add-apt-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y python \  
&& apt-get install -y python3-pip \  
&& apt-get clean \  
&& apt-get install -y wget curl unzip gcc python-dev python-setuptools emacs
vim git less lynx hdfview zlib1g-dev libncurses5-dev libncursesw5-dev cmake
tar gawk valgrind sed python-numpy python-scipy python-pandas build-essential
hdf5-tools libhdf5-dev hdf5-helpers libhdf5-serial-dev apt-utils python-pip
tabix openjdk-7-jdk r-base r-base-dev \  
&& pip install RSeQC  
  
#Install samtools  
RUN wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
\  
&& bunzip2 samtools-1.3.1.tar.bz2 \  
&& tar -xvf samtools-1.3.1.tar \  
&& cd samtools-1.3.1 \  
&& make  
  
#Install bam-readcount  
RUN mkdir git \  
&& cd git \  
&& git clone \--recursive git://github.com/genome/bam-readcount.git \  
&& cd / \  
&& mkdir bam-readcount \  
&& cd bam-readcount \  
&& cmake /git/bam-readcount \  
&& make  
  
#Install STAR  
RUN wget https://github.com/alexdobin/STAR/archive/2.5.1b.tar.gz \  
&& tar -zxvf 2.5.1b.tar.gz \  
&& cd STAR-2.5.1b/source \  
&& make STAR \  
&& file STAR  
  
#Install HTSeq  
RUN wget https://pypi.python.org/packages/source/H/HTSeq/HTSeq-0.6.1p1.tar.gz
\  
&& tar -zxvf HTSeq-0.6.1p1.tar.gz \  
&& cd HTSeq-0.6.1p1/ \  
&& python setup.py install --user \  
&& chmod +x scripts/htseq-count  
  
# Install fastqc  
RUN wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip \  
&& unzip fastqc_v0.11.5.zip \  
&& cd FastQC/ \  
&& chmod 755 fastqc  
  
# Install picard  
RUN wget
https://github.com/broadinstitute/picard/releases/download/1.140/picard-
tools-1.140.zip -O picard-tools-1.140.zip \  
&& unzip picard-tools-1.140.zip  
  
# Install flexbar  
RUN wget
https://github.com/seqan/flexbar/releases/download/v2.4.0/flexbar_v2.4_linux64.tgz
\  
&& tar -xzvf flexbar_v2.4_linux64.tgz \  
&& cd flexbar_v2.4_linux64 \  
&& export LD_LIBRARY_PATH=/flexbar_v2.4_linux64:$LD_LIBRARY_PATH  
  
# Install kallisto  
RUN git clone https://github.com/pachterlab/kallisto.git \  
&& cd kallisto \  
&& mkdir build \  
&& cd build \  
&& cmake .. \  
&& make \  
&& make install  
  
# Get various R packages needed from RNA-seq analysis  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('ggplot2')"  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get -y install libxml2-dev libcurl4-openssl-dev libssl-dev  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite('limma')"  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite('DESeq2')"  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite('edgeR')"  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite('devtools')"  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite('pachterlab/sleuth')"  
  
RUN wget
ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.4-Linux_x86_64.zip
\  
&& unzip hisat2-2.0.4-Linux_x86_64.zip  
  
RUN wget http://cole-trapnell-
lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz \  
&& tar -zxvf cufflinks-2.2.1.Linux_x86_64.tar.gz  
  
RUN git clone https://github.com/biocore/sortmerna \  
&& cd sortmerna \  
&& ./build.sh  
  
RUN git clone https://github.com/timflutre/trimmomatic.git \  
&& cd trimmomatic \  
&& make INSTALL="/" \  
&& make check \  
&& make install \  
&& mv /root/bin/trimmomatic.jar /trimmomatic  
  
RUN wget http://downloads.sourceforge.net/project/samstat/samstat-1.5.1.tar.gz
\  
&& tar -xzvf samstat-1.5.1.tar.gz \  
&& cd samstat-1.5.1 \  
&& ls /samtools-1.3.1 \  
&& sed -i '2847s/.*/SAMTOOLS=samtools/' configure \  
&& ./configure \  
&& make  
  
RUN mkdir RSeqC && mv /usr/local/bin/* RSeqC/  
RUN rm *.gz *.tgz *.tar *.zip  
  
ENV PATH="/samtools-1.3.1:/bam-
readcount/bin:/bowtie2-2.2.9:/tophat-2.1.1.Linux_x86_64:/STAR-2.5.1b/source:/cufflinks-2.2.1.Linux_x86_64:/HTSeq-0.6.1p1/scripts:/FastQC:/picard-
tools-1.140:/samstat-1.5.1/src:/cromwell:/flexbar_v2.4_linux64:/kallisto:/sortmerna:/trimmomatic:/hisat2-2.0.4:/usr/local/bin:${PATH}"  

