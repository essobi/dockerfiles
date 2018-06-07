FROM phusion/baseimage:0.9.17  
MAINTAINER John Kirkham <jakirkham@gmail.com>  
  
  
RUN apt-get update -y && \  
apt-get clean  
  
ADD gridengine /usr/share/gridengine  
RUN /usr/share/gridengine/install_ge.sh  
  
ENV SGE_CONFIG_DIR=/usr/share/gridengine \  
SGE_ROOT=/var/lib/gridengine \  
SGE_CELL=default \  
DRMAA_LIBRARY_PATH=/usr/lib/libdrmaa.so.1.0  
  
ADD miniconda /usr/share/miniconda  
RUN /usr/share/miniconda/install_miniconda.sh  
  
ENV PATH=/opt/conda/bin:$PATH \  
CONDA_DEFAULT_ENV=root \  
CONDA_ENV_PATH=/opt/conda  
  
RUN conda install -y drmaa && \  
conda clean -tipsy  
  
ADD docker /usr/share/docker  
  
ENTRYPOINT [ "/sbin/my_init", "--", "/usr/share/docker/entrypoint.sh" ]  
CMD [ "/bin/bash" ]  

