# Megatid image to suck in fastq and produce DNA-DNA interactions, chromatin
accessibility, and RNA expression  
FROM ubuntu:latest  
MAINTAINER Diego Borges <dborgesr@mit.edu>  
USER root  
  
# Install few tools using apt-get required to get conda package manager up and
running  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common \  
wget \  
bzip2 \  
build-essential \  
vim \  
libboost-dev \  
libcairo2-dev \  
curl \  
zip \  
unzip \  
# libzmq3-dev #iperl \  
# libcairo2-dev #iperl \  
texlive-full #for printing pdf SUPER heavy (over 1Gb) for PDFs \  
&& apt-get update \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Download, install, and update Anaconda3  
ENV CONDA_VERSION="5.1.0"  
RUN wget
https://repo.continuum.io/archive/Anaconda3-${CONDA_VERSION}-Linux-x86_64.sh
&& bash Anaconda3-${CONDA_VERSION}-Linux-x86_64.sh -b && rm
Anaconda3-${CONDA_VERSION}-Linux-x86_64.sh && \  
export PATH=/root/anaconda3/bin:$PATH && \  
conda config --set show_channel_urls True && \  
conda config --add channels r && \  
conda config --add channels bioconda && \  
# conda config --add channels conda-forge && \  
conda update conda && \  
conda update --all --yes && \  
conda install -y pip \  
setuptools \  
nb_conda \  
libgcc \  
conda-build \  
git \  
ipyparallel \  
plotly \  
ipywidgets \  
ipywidgets \  
autoconf \  
bamtools \  
bowtie \  
bowtie2 \  
htslib \  
cython \  
samtools \  
bedops \  
bwa \  
star \  
sra-tools \  
sickle \  
trimmomatic \  
fastqc \  
bedtools \  
bamtools \  
perl-bioperl \  
perl-app-cpanminus \  
libmagic \  
wkhtmltopdf && \  
conda install -c biobuilds perl=5.22.0 && \  
conda install -y -c conda-forge \  
fortran-magic \  
make && \  
conda update -y --all && \  
conda clean -tipy && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi  
ENV PATH=/root/anaconda3/bin:$PATH  
  
RUN pip install --no-cache-dir \  
ipywidgets \  
# seaborn \  
pysam \  
myvariant \  
mygene \  
# weblogo \  
h5py \  
# wand \  
# rst2pdf \  
argparse \  
python-louvain \  
joblib \  
biopython \  
pyliftover \  
# nbbrowserpdf \  
# bx-python \  
numpy-stl \  
solidpython \  
jupyter_contrib_nbextensions \  
jupyter-c-kernel \  
jupyterlab  
# && pip freeze --local | grep -v '^\\-e' | cut -d = -f 1 | xargs -n1 pip
install -U  
#install r kernel stuff  
RUN conda install -y -c r \  
'r-base' \  
'r-irkernel' \  
'r-plyr' \  
'r-devtools' \  
'r-tidyverse' \  
'r-shiny' \  
'r-rmarkdown' \  
'r-forecast' \  
'r-rsqlite' \  
'r-reshape2' \  
'r-nycflights13' \  
'r-caret' \  
'r-rcurl' \  
'r-crayon' \  
'r-randomforest' \  
&& conda clean -y -t -i -l -a  
  
#install bash kernel  
RUN pip install bash_kernel && \  
python -m bash_kernel.install  
  
#Install perl package manager and perl kernel takes super long and currently
broken  
#RUN curl -sL http://cpanmin.us | perl - App::cpanminus \  
# && /usr/local/bin/cpanm --notest Devel::IPerl \  
# PDL \  
# Moose \  
# MooseX::AbstractFactory \  
# MooseX::AbstractMethod \  
# MooseX::Storage \  
# Test::More  
#Enable C kernel after installed using pip above (jupyter-c-kernel)  
RUN install_c_kernel  
  
#Install python 2.7 kernel and environment  
RUN conda create -y -n py27 python=2.7 \  
ipykernel \  
numpy \  
scipy \  
pandas \  
h5py \  
bx-python \  
pysam \  
macs2 \  
&& conda clean -y -t -i -l -a  
  
#Install C kernel  
#RUN cd /root && wget -O - https://raw.githubusercontent.com/brendan-
rius/jupyter-c-kernel/master/install.sh | sh  
#Configure jupyter  
RUN jupyter notebook --generate-config --allow-root && \  
sed -i "/c.NotebookApp.open_browser/c c.NotebookApp.open_browser = False"
/root/.jupyter/jupyter_notebook_config.py \  
&& sed -i "/c.NotebookApp.ip/c c.NotebookApp.ip = '*'"
/root/.jupyter/jupyter_notebook_config.py \  
&& sed -i "/c.NotebookApp.notebook_dir/c c.NotebookApp.notebook_dir =
'/root/Euplotid'" /root/.jupyter/jupyter_notebook_config.py \  
&& sed -i "/c.NotebookApp.token/c c.NotebookApp.token = 'euplotid'"
/root/.jupyter/jupyter_notebook_config.py \  
&& sed -i "/c.NotebookApp.iopub_data_rate_limit/c
c.NotebookApp.iopub_data_rate_limit = 10000000"
/root/.jupyter/jupyter_notebook_config.py \  
&& jupyter nbextension enable \--py widgetsnbextension \  
&& jupyter contrib nbextension install --system \  
&& jupyter nbextension install nbpresent --py --overwrite --system \  
&& jupyter nbextension enable nbpresent --py --system \  
&& jupyter serverextension enable nbpresent --py --system  
  
#Install Jupyterlab google drive extension  
RUN conda install -y nodejs && jupyter labextension install
@jupyterlab/google-drive  
  
#Get Homer  
RUN cd /root && mkdir Homer && wget
http://homer.ucsd.edu/homer/configureHomer.pl && perl configureHomer.pl
-install homer  
ENV PATH=~/Homer/bin/:$PATH  
  
#Get Chrom3D  
#RUN cd /root && git clone https://github.com/CollasLab/Chrom3D.git && cd
./Chrom3D && make  
#Get ChiAPet2  
RUN cd /root && git clone https://github.com/GuipengLi/ChIA-PET2.git && cd
./ChIA-PET2 && chmod 755 ./bin/ChIA-PET2 && make  
ENV PATH=~/ChIA-PET2/bin/:$PATH  
  
#Get Origami compilation broken  
#RUN cd /root && git clone https://github.com/danielsday/origami.git && cd
origami && autoconf && ./configure --prefix=/root/origami
CPPFLAGS=-I=/root/bamtools/include  
#Install Cooler in py27 enviro  
#RUN /bin/bash -c "source activate py27 && pip install cooler && source
deactivate"  
#install NucleoATAC in py27 enviro  
#RUN /bin/bash -c "source activate py27 && cd /root && git clone
https://github.com/GreenleafLab/NucleoATAC.git && cd NucleoATAC && pip install
. && source deactivate py27"  
#Get mirSTP  
RUN cd /root && wget http://bioinfo.vanderbilt.edu/mirSTP/download/mirSTP.zip
&& unzip mirSTP.zip && rm mirSTP.zip && chmod 755 mirSTP/bin/mirSTP  
ENV PATH=~/mirSTP/bin:$PATH  
  
#Get pytorch  
RUN conda install pytorch torchvision -y -c soumith  
  
#Get Euplotid  
RUN cd /root && git clone -b master --single-branch
https://github.com/dborgesr/Euplotid.git  
  
#run a closing update  
RUN conda update -y --all \  
&& conda clean -y -t -i -l -a  
  
# Set root as workdir  
WORKDIR /root/Euplotid  
  
EXPOSE 8891  
CMD ["jupyter", "lab", "--port=8891", "--no-browser", "--allow-root", "--
ip=0.0.0.0"]

