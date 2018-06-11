FROM ubuntu:16.04  
RUN apt-get update  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a
/etc/apt/sources.list  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | apt-key add -  
RUN apt-get update  
RUN apt-get -y install r-base git wget tar g++ make python python-pip
zlib1g-dev git  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('argparse')"  
RUN Rscript -e "install.packages('data.table')"  
  
RUN pip install argparse synapseclient numpy gffutils biopython  
  
WORKDIR /opt  
  
RUN wget
https://github.com/samtools/bcftools/releases/download/1.5/bcftools-1.5.tar.bz2
-O bcftools.tar.bz2 && \  
tar -xjvf bcftools.tar.bz2 &&\  
cd bcftools-1.5 && \  
make && \  
make prefix=/usr/local/bin install && \  
ln -s /usr/local/bin/bin/bcftools /usr/bin/bcftools  
  
RUN wget https://github.com/deweylab/RSEM/archive/v1.2.31.tar.gz && \  
tar -zxvf v1.2.31.tar.gz && \  
cd RSEM-1.2.31/ && \  
make && \  
make install  
  
RUN wget https://github.com/alexdobin/STAR/archive/STAR_2.4.2a.tar.gz && \  
tar -zxvf STAR_2.4.2a.tar.gz && \  
cp /opt/STAR-STAR_2.4.2a/bin/Linux_x86_64/* /usr/local/bin  
  
RUN git clone https://github.com/andrewelambsage/rnaseqSim/ && \  
chmod +x /opt/rnaseqSim/fusion_create/*.py* && \  
chmod +x /opt/rnaseqSim/model_isoforms/*.R && \  
chmod +x /opt/rnaseqSim/fastq_create/*.py && \  
chmod +x /opt/rnaseqSim/genome_create/*.py  
  
ENV PATH /opt/rnaseqSim/fusion_create:$PATH  
ENV PATH /opt/rnaseqSim/model_isoforms:$PATH  
ENV PATH /opt/rnaseqSim/fastq_create:$PATH  
ENV PATH /opt/rnaseqSim/genome_create:$PATH  

