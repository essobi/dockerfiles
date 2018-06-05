####################################################################  
# Based on Debian GNU/Linux version 8 3.10.0-514.21.1.el7.x86_64 #  
####################################################################  
FROM continuumio/miniconda3  
MAINTAINER Grace McCalla <smccalla@usgs.gov>  
LABEL Description="Dockerfile to analyze amplicon data"  
RUN apt-get update && apt-get upgrade -y --force-yes && apt-get install -y \  
g++ \  
make \  
git \  
bwa \  
samtools \  
python3-pip \  
python-numpy \  
build-essential \  
default-jre \  
zlib1g-dev \  
sra-toolkit \  
python3-matplotlib \  
unzip \  
wget \  
curl \  
gcc \  
python3-dev \  
libgsl0-dev \  
python-biopython \  
&& rm -rf /var/lib/apt/lists/*  
  
# Disable SSL for anaconda due to DOI man in the middle  
RUN conda config --set ssl_verify false  
  
# Install QIIME - the Anaconda version  
# See http://qiime.org/install/install.html for details  
RUN conda create -y -n qiime1 python=2.7 qiime matplotlib=1.4.3 mock nose -c
bioconda  
# Change the matplotlib backend so Qiime plotting scripts will execute  
RUN sed -i.bak s/': Qt4Agg'/': agg'/g
/opt/conda/envs/qiime1/lib/python2.7/site-packages/matplotlib/mpl-
data/matplotlibrc  
  
RUN conda config --add channels conda-forge  
RUN conda install backports.shutil_get_terminal_size  
  
# Install biopython  
ENV PYTHON_PATH /biopython  
SHELL ["/bin/bash", "-c"]  
RUN git clone https://github.com/biopython/biopython.git  
WORKDIR /biopython  
RUN source activate qiime1  
RUN conda install -q -y biopython  
RUN conda install --yes python=2.7 biopython  
#RUN conda install --yes python=3.5 biopython  
RUN pip install bioseq  
RUN conda install -y biopython==1.66  
RUN easy_install pip  
RUN pip2 install biopython  
RUN pip3 install biopython  
  
# Install BLAST  
RUN conda install -c bioconda blast-legacy=2.2.22  
  
# Download & install fastq-join  
WORKDIR /root/  
RUN cd ~ && \  
wget
"https://drive.google.com/uc?export=download&id=0B7KhouP0YeRAc2xackxzRnFrUEU"
-O ea-utils.1.1.2-806.tar.gz && \  
tar -xvf ea-utils.1.1.2-806.tar.gz && \  
cd ea-utils.1.1.2-806 && \  
make && \  
cp -a fastq-mcf /usr/local/bin/ && \  
cp -a fastq-join /usr/local/bin/ && \  
cd ~ && \  
rm -rf ea-utils.1.1.2-806 ea-utils.1.1.2-806.tar.gz  
ENV PATH "$PATH:/usr/local/bin/fastQValidator"  
ENV PATH /usr/local/bin/fastQValidator:$PATH  
  
# Download & install BLAST  
RUN mkdir /opt/blast \  
&& curl ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz \  
| tar -zxC /opt/blast --strip-components=1  
ENV PATH "$PATH:/opt/blast/bin"  
ENV PATH /opt/blast/bin:$PATH  
ENV PATH="/opt/blast/bin:${PATH}"  
# Download & install Trimmomatic  
RUN wget
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
\  
&& unzip Trimmomatic-0.36.zip \  
&& chmod -R +x Trimmomatic-0.36 \  
&& mv Trimmomatic-0.36/trimmomatic-0.36.jar /usr/local/bin/  
ENV PATH "$PATH:/usr/local/bin/Trimmomatic-0.36"  
ENV PATH /usr/local/bin/Trimmomatic-0.36:$PATH  
  
# Build libStatGen  
RUN git clone https://github.com/statgen/libStatGen /usr/local/bin/libStatGen  
RUN make -C /usr/local/bin/libStatGen  
ENV PATH "$PATH:/usr/local/bin/libStatGen"  
ENV PATH /usr/local/bin/libStatGen:$PATH  
  
# Download & install FastQC  
# https://hub.docker.com/r/genomicpariscentre/fastqc/~/dockerfile/  
# https://hub.docker.com/r/biocontainers/fastqc/~/dockerfile/  
ENV DST=/tmp  
ENV URL=http://www.bioinformatics.babraham.ac.uk/projects/fastqc/  
ENV ZIP=fastqc_v0.11.5.zip  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
unzip - $DST/$ZIP -d $DST && \  
rm $DST/$ZIP && \  
cd $DST/FastQC && \  
chmod 755 fastqc && \  
ln -s $DST/FastQC/fastqc /usr/local/bin/fastqc  
ENV PATH "$PATH:/usr/local/bin/FastQC"  
ENV PATH /usr/local/bin/FastQC:$PATH  
  
# Download & install fastQValidator  
RUN git clone https://github.com/statgen/fastQValidator.git
/usr/local/bin/fastQValidator  
RUN make -C /usr/local/bin/fastQValidator && \  
chmod +x -R /usr/local/bin/  
ENV PATH "$PATH:/usr/local/bin/fastQValidator"  
ENV PATH /usr/local/bin/fastQValidator:$PATH  
  
# Download & install Assign Taxonomy  
RUN git clone https://github.com/Joseph7e/Assign-Taxonomy-with-BLAST
/usr/local/bin/taxonomy_assignment && \  
chmod +x -R /usr/local/bin/taxonomy_assignment  
ENV PATH "$PATH:/usr/local/bin/taxonomy_assignment"  
ENV PATH /usr/local/bin/taxonomy_assignment/:$PATH  
  
# Download & install steps1-4 for analyzing amplicon data  
RUN git clone https://github.com/sgmccalla/amplicon_pipeline
/usr/local/bin/amplicon_pipeline && \  
chmod +x -R /usr/local/bin/amplicon_pipeline  
ENV PATH "$PATH:/usr/local/bin/amplicon_pipeline"  
ENV PATH /usr/local/bin/amplicon_pipeline/:$PATH  
  
# Activate Qiime1  
RUN git clone https://github.com/sgmccalla/amplicon_dockerfile
/usr/local/bin/run_qiime && \  
chmod +x -R /usr/local/bin/run_qiime  
ENV PATH "$PATH:/usr/local/run_qiime"  
ENV PATH /usr/local/bin/run_qiime:$PATH  
RUN /usr/local/bin/run_qiime/run_qiime.sh

