# Here we define the base image, in this case one specific Debian distro  
# This aspect is important for reproducibility / stability  
FROM rocker/tidyverse:latest  
  
MAINTAINER VIB Bioinformatics Core <bits@vib.be>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
git mercurial subversion  
  
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
/opt/conda/bin/conda clean -tipsy && \  
ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \  
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \  
echo "conda activate base" >> ~/.bashrc  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
  
RUN chmod +x /usr/bin/tini  
  
ENV PATH /opt/conda/bin:$PATH  
RUN conda config --add channels conda-forge  
  
RUN pip install git+git://github.com/PMBio/MOFA  
  
RUN R -e " \  
devtools::install_github('PMBio/MOFA', subdir='MOFAtools'); \  
"  

