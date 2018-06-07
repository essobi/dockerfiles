# Container for your repository to work with everware.  
# Your analysis container should inherit this one with  
# `FROM eabdullin/everware-miniconda`  
FROM continuumio/miniconda  
MAINTAINER Yelaman Abdullin <a.elaman.b@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
# Update anaconda  
ENV CONDA_DIR /opt/conda  
  
RUN /bin/bash -c "conda install --yes ipython-notebook ipywidgets=4.1.0 && \  
ipython kernelspec install-self"  
  
RUN $CONDA_DIR/bin/conda update conda && \  
conda update --all  
  
# This kernel becomes available in the notebook with what ever  
# packages are installed in the conda environment  
# The python3 kernel is not necessary but nice to have  
RUN /bin/bash -c "conda create -n py3 python=3.4 && \  
source activate py3 && \  
conda install --yes ipython-notebook && \  
ipython kernelspec install-self"  
  
RUN mkdir -p /srv/  
WORKDIR /srv/  
  
# fetch juptyerhub-singleuser entrypoint  
ADD
https://raw.githubusercontent.com/jupyter/jupyterhub/master/scripts/jupyterhub-
singleuser /usr/local/bin/jupyterhub-singleuser  
RUN chmod 755 /usr/local/bin/jupyterhub-singleuser  
  
# jupyter is our user  
RUN useradd -m -s /bin/bash jupyter  
  
USER jupyter  
ENV HOME /home/jupyter  
ENV SHELL /bin/bash  
ENV USER jupyter  
  
WORKDIR /home/jupyter/  
  
EXPOSE 8888  
ADD singleuser.sh /srv/singleuser/singleuser.sh  
CMD ["sh", "/srv/singleuser/singleuser.sh"]

