FROM ubuntu:12.04  
MAINTAINER John Kirkham <jakirkham@gmail.com>  
  
  
RUN apt-get update -y && \  
apt-get clean  
  
ADD miniconda /usr/share/miniconda  
RUN /usr/share/miniconda/install_miniconda.sh  
  
ENV PATH=/opt/conda/bin:$PATH \  
CONDA_DEFAULT_ENV=root \  
CONDA_ENV_PATH=/opt/conda  
  
ADD docker /usr/share/docker  
RUN /usr/share/docker/install_tini.sh  
  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
CMD [ "/bin/bash" ]  

