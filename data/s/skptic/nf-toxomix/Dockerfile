FROM continuumio/miniconda  
  
LABEL authors="evan.floden@gmail.com" \  
description="Docker image containing all requirements for NF-toxomix pipeline"  
# Install container-wide requrements gcc, pip, zlib, libssl, make, libncurses,
fortran77, g++, R  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends \  
g++ \  
gcc \  
gfortran \  
libbz2-dev \  
libcurl4-openssl-dev \  
liblzma-dev \  
libncurses5-dev \  
libpcre3-dev \  
libreadline-dev \  
libssl-dev \  
make \  
python-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install pip  
RUN curl -fsSL https://bootstrap.pypa.io/get-pip.py -o /opt/get-pip.py && \  
python /opt/get-pip.py && \  
rm /opt/get-pip.py  
#RUN wget http://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh
-O ~/miniconda.sh && \  
# bash ~/miniconda.sh -b -p /miniconda && \  
# export PATH="/miniconda/bin:$PATH"  
# Install Kallisto  
RUN conda config \--add channels defaults \  
&& conda config \--add channels bioconda \  
&& conda config \--add channels conda-forge \  
&& conda install kallisto r r-essentials r-irkernel r-sleuth  
  
# Install Sleuth  
#RUN R -e 'source("http://bioconductor.org/biocLite.R");
library(BiocInstaller); biocLite(c("XML","biomaRt")); biocLite("rhdf5");
install.packages("devtools", repos="http://cloud.r-project.org/");
devtools::install_github("pachterlab/sleuth")'  
# Install FastQC  
RUN apt-get update && \  
apt-get install -y \--no-install-recommends unzip && \  
curl -fsSL
http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip -o
/opt/fastqc_v0.11.5.zip && \  
unzip /opt/fastqc_v0.11.5.zip -d /opt/ && \  
chmod 755 /opt/FastQC/fastqc && \  
ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc && \  
rm /opt/fastqc_v0.11.5.zip  
  
# Install MultiQC  
RUN pip install git+git://github.com/ewels/MultiQC.git  

