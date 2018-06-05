FROM jupyter/minimal-notebook  
  
# Some stuff from https://github.com/jupyter/docker-stacks/blob/master/scipy-
notebook/Dockerfile  
MAINTAINER Chris Mutel <cmutel@gmail.com>  
  
USER root  
  
# Need mercurial for hg to get test coverage info  
RUN apt-get update && apt-get install -y mercurial  
  
USER $NB_USER  
RUN conda install --quiet --yes wheel && \  
conda update --yes pip wheel setuptools  
  
# Install Python 3 packages  
RUN conda install -y -q -c conda-forge -c cmutel -c haasad brightway2 jupyter
pytest pytest-cov python-coveralls && \  
conda clean -tipsy  
  
RUN mkdir /home/jovyan/data  
RUN mkdir /home/jovyan/notebooks  
RUN mkdir /home/jovyan/output  
  
ENV BRIGHTWAY2_DIR /home/jovyan/data  
ENV BRIGHTWAY2_DOCKER 1  
ENV BRIGHTWAY2_OUTPUT_DIR /home/jovyan/output  
  
  
WORKDIR /home/jovyan/notebooks  

