#################################################################  
# Dockerfile  
#  
# Version: 0.0.1  
# Software: pAss  
# Software Version: 0.0.2  
# Description: A gene centric metagenomics assembly and annotation pipeline  
# Website: https://github.com/etheleon/pAss  
# Tags: Genomics Metagenomics  
# Provides: bowtie 1.1.2  
# Base Image: biodckr/biodocker  
#Run CMD: ROOTDIR=/Users/uesu/github/reAssemble/justK03043  
# docker run -v $ROOTDIR/data/contigs:/data/contigs \  
# -v $ROOTDIR/data/konr:/data/refSeqProtDB \  
# -v $ROOTDIR/out:/data/out \  
# -v $ROOTDIR/misc:/data/misc newpass:latest \  
# maxDiversity --outputDIR /data/out --format --threads 8 \--refseqKO
/data/refSeqProtDB --contigs /data/contigs --megan /usr/local/bin/MEGAN
--meganLicense /data/misc/MEGAN5-academic-license.txt  
#################################################################  
  
# Build image with: docker build -t krizsan/ubuntu1504java8:v1 .  
  
FROM ubuntu:16.04  
  
#Java###############################  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean  
  
#NCBI##############################  
RUN apt-get install -y ncbi-blast+  
  
WORKDIR /tmp  
  
#MEGAN#############################  
RUN apt-get update && apt-get install -y xvfb  
RUN wget -nv http://ab.inf.uni-
tuebingen.de/data/software/megan5/download/MEGAN_unix_5_11_3.sh  
RUN perl -E 'say join "\n", "", 1, "", 1, "", "", "", 38000, n, ""' >
/tmp/megan_install_v5  
#COPY megan_install_v5 /tmp  
RUN bash MEGAN_unix_5_11_3.sh < /tmp/megan_install_v5  
  
#Dependencies############################  
  
RUN apt-get update && \  
apt-get install -y r-base && \  
apt-get install -y curl && \  
apt-get install -y make  
RUN apt-get install -y r-cran-ggplot2  
  
RUN wget
http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz &&
\  
tar zvxf muscle3.8.31_i86linux64.tar.gz  
RUN cp /tmp/muscle3.8.31_i86linux64 /usr/bin/muscle  
  
RUN apt-get install perl-doc  
RUN apt-get install -y git  
#RUN groupadd -r maxdiversity && adduser --ingroup maxdiversity --disabled-
password --gecos "" wesley  
#USER wesley  
  
#PASS  
RUN git clone https://github.com/etheleon/pAss.git /tmp/pAss  
  
RUN curl -L https://cpanmin.us | perl - App::cpanminus && \  
cpanm local::lib Carton Module::Install  
  
WORKDIR /tmp/pAss  
RUN carton  
RUN cpanm Minilla  
RUN minil install  
#RUN perl Makefile.PL PREFIX=./local/ && \  
#make && \  
#make install  
  
ENV PATH=/usr/local/megan:/tmp/pAss:${PATH}  
ENV PERL5LIB=/tmp/pAss/local/lib/perl5:/tmp/pAss/local/share/perl/5.22.1  
RUN R -e 'install.packages("dplyr", repos="http://cran.bic.nus.edu.sg/")'  
RUN R -e 'source("http://bioconductor.org/biocLite.R");
biocLite("Biostrings")'  
  
VOLUME ["/data/contigs", "/data/refSeqProtDB", "/data/out", "data/misc"]  
ENTRYPOINT ["/tmp/pAss/script/maxDiversity"]  
CMD ["--outputDIR", "/data/out", "--format", "--refseqKO",
"/data/refSeqProtDB", "--contigs", "/data/contigs", "--megan",
"/usr/local/bin/MEGAN", "--meganLicense", "/data/misc/MEGAN5-academic-
license.txt"]  
  
#################### INSTALLATION ENDS ##############################  
MAINTAINER Wesley GOI <wesley@bic.nus.edu.sg>  

