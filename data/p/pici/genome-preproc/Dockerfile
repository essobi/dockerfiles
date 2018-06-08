FROM ubuntu:16.04  
MAINTAINER Danny Wells "danny@parkerici.org"  
#Python, R, Java, other dependencies  
RUN apt-get update \  
&& apt-get install -y --force-yes software-properties-common \  
&& echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list \  
&& gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 \  
&& gpg -a --export E084DAB9 | apt-key add - \  
&& add-apt-repository ppa:openjdk-r/ppa \  
&& apt-get update \  
&& apt-get install -y git wget unzip vim sudo net-tools python r-base r-base-
dev openjdk-7-jdk maven g++ zlib1g-dev make build-essential gcc python-
setuptools python-dev cmake tabix libz-dev vcftools curl libcurl4-openssl-dev
libssl-dev \  
&& easy_install pip \  
&& pip install numpy  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y fastqc tabix git  
RUN apt-get install -y python  
  
#Install bedtools  
RUN git clone https://github.com/arq5x/bedtools2.git && \  
cd bedtools2 && \  
make && \  
mkdir /bedtools && \  
cp bin/* /bedtools/  
  
#Install GATK  
RUN git clone https://github.com/broadgsa/gatk-protected \  
&& cd /gatk-protected \  
&& git reset --hard 3.1 \  
&& mvn -Ddisable.queue install  
  
#Install picard  
RUN cd / && \  
wget https://github.com/broadinstitute/picard/releases/download/1.140/picard-
tools-1.140.zip -O picard-tools-1.140.zip && \  
unzip picard-tools-1.140.zip  
  
#Install samtools  
RUN cd / && \  
wget
https://github.com/samtools/samtools/releases/download/1.3.1/samtools-1.3.1.tar.bz2
&& \  
bunzip2 samtools-1.3.1.tar.bz2 && \  
tar -xvf samtools-1.3.1.tar && \  
cd samtools-1.3.1 && \  
make  
  
#Install fastqc  
RUN cd / && \  
wget
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip &&
\  
unzip fastqc_v0.11.5.zip && \  
cd FastQC/ && \  
chmod 755 fastqc  
  
#Install BAMTools  
RUN cd / && \  
git clone git://github.com/pezmaster31/bamtools.git && \  
cd bamtools && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make  
  
ENV PATH="/bedtools:/samtools-1.3.1:/picard-
tools-1.140:/bamtools/bin:/FastQC:/gatk-protected/target:${PATH}"  

