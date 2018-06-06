FROM ubuntu:14.04  
  
RUN apt-get update && \  
apt-get -y install \  
latex-xcolor \  
libgomp1 \  
texlive-fonts-recommended \  
texlive-latex-base \  
texlive-latex-extra  
  
# conda, from https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
# packages for autoseq  
RUN conda config --add channels r && \  
conda config --add channels bioconda && \  
conda info -a && \  
conda install -y -c bioconda \  
bcftools=1.2 \  
bedtools=2.25.0 \  
bioconductor-qdnaseq \  
bioconductor-variantannotation=1.16.4 \  
bwa=0.7.12 \  
cffi \  
click \  
cnvkit=0.7.9 \  
cryptography \  
fastqc=0.11.4 \  
freebayes=1.0.1 \  
htslib=1.2.1 \  
lofreq=2.1.2 \  
matplotlib \  
multiqc \  
nose \  
openpyxl \  
parallel \  
picard=2.3.0 \  
pindel=0.2.5a7 \  
pip \  
psycopg2 \  
pycparser \  
pysam=0.8.4 \  
pytest \  
pyvcf=0.6.8.dev0 \  
r-data.table \  
r-devtools \  
r-devtools \  
r-getopt \  
r-ggplot2=2.1.0 \  
r-httr \  
r-plyr \  
r-pscbs \  
r-rcurl \  
r-reshape \  
r-rjsonio=1.3_0 \  
r=3.2.2 \  
sambamba=0.5.9 \  
samblaster=0.1.22 \  
samtools=1.2 \  
scalpel=0.5.1 \  
skewer=0.1.126 \  
star=2.4.2a \  
ucsc-gtftogenepred \  
vardict-java=1.4.3 \  
vardict=2016.02.19 \  
variant-effect-predictor=83 \  
vcflib=1.0.0_rc0 \  
vt=2015.11.10  
  
RUN conda install -y -c dakl autoseq-scripts  
  
CMD [ "/bin/bash" ]  

