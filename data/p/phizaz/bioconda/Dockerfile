FROM phizaz/bioconda:base  
  
########################################  
# ROOT MODE  
########################################  
  
###### SETUP CONDA PYTHON 2 ###############  
RUN cd /tmp \  
&& curl -O https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh \  
&& bash Miniconda2-latest-Linux-x86_64.sh -b -p /opt/conda  
ENV PATH=/opt/conda/bin:$PATH  
RUN conda config --add channels defaults \  
&& conda config --add channels conda-forge \  
&& conda config --add channels bioconda  

