FROM ubuntu:16.04  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
# Install procps (to get free and top)  
RUN apt-get update --fix-missing && \  
apt-get install -y procps  
  
# Install miniconda. Copied from
https://hub.docker.com/r/continuumio/miniconda/~/dockerfile/ (because we need
debian:stretch to install gcc 6 which is needed for HiCPro)  
RUN apt-get install -y wget bzip2 ca-certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-4.3.27-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN apt-get install -y curl grep sed dpkg && \  
TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o
"/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
ENV PATH /opt/conda/bin:$PATH  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  
RUN apt-get update && apt-get install -y gcc && apt-get clean  
  
RUN conda config --add channels bioconda  
RUN conda install -c bioconda bx-python  
RUN conda install -c bioconda scipy  
RUN conda install -c bioconda numpy  
RUN conda install -c bioconda pysam  
RUN conda install gxx_linux-64  
  
# Install Bowtie2  
RUN apt-get install -y gcc libtbb-dev unzip && \  
mkdir /src && \  
cd /src && \  
wget -O bowtie2.zip https://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.3.2/bowtie2-2.3.2-linux-x86_64.zip/download && \  
unzip bowtie2.zip && \  
ln -s /src/bowtie2-2.3.2/bowtie2* /usr/local/bin  
  
# Install R-3.4.0 (See https://cran.r-project.org/bin/linux/ubuntu)  
COPY E084DAB9.gpg /root/  
RUN apt-get install -y apt-transport-https gnupg libssl-dev libcurl4-openssl-
dev libxml2-dev && \  
echo "deb https://cloud.r-project.org/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list && \  
apt-key add /root/E084DAB9.gpg && \  
apt-get update && \  
apt-get install -y --force-yes r-base  
  
#Installing necessary R packages  
RUN Rscript -e "source('http://bioconductor.org/biocLite.R');
biocLite(c('ggplot2', 'RColorBrewer', 'remotes', 'optparse'));
remotes::install_github('aryeelab/sparsehic', ref='874de99')"  
  
# Install HiCPro  
RUN cd /tmp && \  
wget -O HiC-Pro.tar.gz https://github.com/nservant/HiC-
Pro/archive/v2.10.0.tar.gz && \  
tar zxf HiC-Pro.tar.gz && \  
cd HiC-Pro-2.10.0 && \  
sed -i 's/PREFIX =/PREFIX = \//g' config-install.txt && \  
make configure && \  
make install && \  
cd .. && \  
rm -fr HiC-Pro* && \  
ln -s /HiC-Pro_2.10.0 /HiC-Pro  
  
# Upgrade iced to v0.4.3 (to fix memory leak bug)  
RUN pip install iced==0.4.3  
  
# Install a compatible version of gawk  
RUN cd /tmp && \  
wget http://ftp.gnu.org/gnu/gawk/gawk-3.1.7.tar.gz && \  
tar zxf gawk-3.1.7.tar.gz && \  
cd gawk-3.1.7 && \  
./configure --prefix=/usr --libexecdir=/usr/lib && \  
make && \  
make install && \  
cd .. && \  
rm -fr gawk-3.1.7* && \  
ln -sf /usr/bin/gawk /etc/alternatives/awk  
  
# Install juicer tools  
RUN apt-get update --fix-missing && \  
apt-get install -y default-jre && \  
mkdir -p /usr/local/juicer && \  
cd /usr/local/juicer && \  
wget
http://hicfiles.tc4ga.com.s3.amazonaws.com/public/juicer/juicer_tools.1.7.6_jcuda.0.8.jar  
  
# Install hicpro to sparsehic script  
COPY hicpro_to_sparsehic.R /usr/local/bin/  
  
# Install bc for summing input fastq sizes  
RUN apt-get install -y bc  
  
COPY Mboi_resfrag_hg19.bed.gz /HiC-Pro/annotation  
COPY hg19.chrom.sizes /HiC-Pro/annotation  
  
COPY Mboi_resfrag_grch38.bed.gz /HiC-Pro/annotation  
COPY grch38.chrom.sizes /HiC-Pro/annotation  
  
COPY Mboi_resfrag_hg38.bed.gz /HiC-Pro/annotation  
COPY hg38.chrom.sizes /HiC-Pro/annotation  
  
COPY Mboi_resfrag_mm10.bed.gz /HiC-Pro/annotation  
COPY mm10.chrom.sizes /HiC-Pro/annotation  
  
RUN cd /HiC-Pro/annotation && \  
gunzip *.bed.gz

