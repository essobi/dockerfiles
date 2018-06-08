FROM ubuntu:16.04  
LABEL base.image="biocontainers:latest"  
LABEL version="1"  
LABEL software="SalmonTE"  
LABEL software.version="0.3"  
LABEL description="An ultra-fast and scalable quantification pipeline for
transposable elements from next generation sequencing data"  
LABEL website="https://github.com/hyunhwaj/SalmonTE"  
LABEL
documentation="https://github.com/hyunhwaj/SalmonTE/blob/master/README.md"  
LABEL license="https://github.com/hyunhwaj/SalmonTE/blob/master/LICENSE"  
LABEL tags="Genomics"  
  
MAINTAINER Wen-Wei Liao <wen-wei.liao@wustl.edu>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bkp && \  
bash -c 'echo -e "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial main
restricted universe multiverse\n\  
deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted
universe multiverse\n\  
deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-backports main restricted
universe multiverse\n\  
deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-security main restricted
universe multiverse\n\n" > /etc/apt/sources.list' && \  
cat /etc/apt/sources.list.bkp >> /etc/apt/sources.list && \  
cat /etc/apt/sources.list  
  
RUN apt-get clean all && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
autotools-dev \  
automake \  
cmake \  
curl \  
grep \  
sed \  
dpkg \  
fuse \  
git \  
wget \  
zip \  
openjdk-8-jre \  
build-essential \  
pkg-config \  
python \  
python-dev \  
python-pip \  
bzip2 \  
ca-certificates \  
libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
git \  
mercurial \  
subversion \  
r-base \  
r-base-dev \  
libnss-sss \  
locales \  
zlib1g-dev && \  
locale-gen en_US.UTF-8 && \  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
RUN TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep
-o "/v.*\"" | sed 's:^..\\(.*\\).$:\1:'` && \  
curl -L
"https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb"
> tini.deb && \  
dpkg -i tini.deb && \  
rm tini.deb && \  
apt-get clean  
  
RUN mkdir /data /config  
  
# Add user biodocker with password biodocker  
RUN groupadd fuse && \  
useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups
sudo,fuse biodocker && \  
echo `echo "biodocker\nbiodocker\n" | passwd biodocker` && \  
chown biodocker:biodocker /data && \  
chown biodocker:biodocker /config  
  
# give write permissions to conda folder  
RUN chmod 777 -R /opt/conda/  
  
ENV PATH=$PATH:/opt/conda/bin  
ENV PATH=$PATH:/home/biodocker/bin  
ENV HOME=/home/biodocker  
  
RUN mkdir /home/biodocker/bin  
  
RUN conda config --add channels r  
RUN conda config --add channels conda-forge  
RUN conda config --add channels bioconda  
  
RUN conda upgrade conda  
  
VOLUME ["/data", "/config"]  
  
RUN conda install snakemake docopt pandas r  
RUN conda install r-tidyverse r-scales r-writexls r-cowplot  
RUN conda install bioconductor-deseq2 bioconductor-tximport  
  
WORKDIR $HOME  
  
RUN git clone https://github.com/hyunhwaj/SalmonTE.git  
ENV PATH=$PATH:$HOME/SalmonTE  
  
WORKDIR /data  

