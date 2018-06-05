FROM ubuntu:16.04  
MAINTAINER Charles Cary "ccary@parkerici.org"  
## TO DO: migrate all packages to the top (one final master compile),  
## Reconcile file structures between different containers so  
## behavior is identical  
## add an ENV command to make all tools available at command line.  
#Python, R, Java, other dependencies  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
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
  
#Install GATK  
RUN git clone https://github.com/broadgsa/gatk-protected \  
&& cd /gatk-protected \  
&& git reset --hard 3.1 \  
&& mvn -Ddisable.queue install  
  
#Install mutect  
RUN git clone https://github.com/broadinstitute/mutect.git \  
&& cd /mutect \  
&& mvn verify  
  
#Install strelka  
RUN git clone https://github.com/genome-vendor/strelka strelka_build\  
&& cd /strelka_build \  
&& mkdir -p /strelka \  
&& ./configure --prefix=/strelka \  
&& make  
  
#Install varscan  
RUN mkdir -p /varscan \  
&& cd /varscan \  
&& wget
https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar  
  
# Install Oncotator  
# We have to build biopython ourselves because the artifacts referenced by
oncotator are broken  
RUN easy_install -f http://biopython.org/DIST/biopython-1.66.tar.gz biopython
\  
&& git clone https://github.com/broadinstitute/oncotator \  
&& cd /oncotator \  
&& git checkout tags/v1.9.1.0 -b v1.9.1.0 \  
&& python setup.py install  
  
# Install sequenza  
RUN R -e "source(\"https://bioconductor.org/biocLite.R\");
biocLite(\"copynumber\")" \  
&& R -e "install.packages('sequenza', repos='https://cran.rstudio.com/');
quit()"  
  
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
  
RUN git clone https://github.com/arq5x/bedtools2.git && \  
cd bedtools2 && \  
make && \  
mkdir /bedtools && \  
cp bin/* /bedtools/  
  
ENV PATH="/bedtools:/usr/local/lib/R/site-
library/sequenza/exec:/samtools-1.3.1:/picard-
tools-1.140:/mutect/target:/strelka/libexec:/varscan:/bamtools/bin:/FastQC:/gatk-
protected/target:${PATH}"  

