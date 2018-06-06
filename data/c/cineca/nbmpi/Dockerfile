  
FROM jupyter/minimal-notebook  
# https://github.com/jupyter/docker-stacks/blob/master/minimal-
notebook/Dockerfile  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@gmail.com>"  
# Libraries  
USER root  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
openmpi-bin openmpi-common openssh-client \  
liblapack-dev libblas-dev \  
&& apt-get clean  
  
RUN mkdir /data && chown jovyan /data  
  
# Python packages  
USER jovyan  
RUN conda install --yes \  
numpy scipy pandas matplotlib seaborn \  
mpi4py \  
&& conda clean -yt  
  
# RISE  
WORKDIR /tmp  
RUN wget -q https://github.com/pdonorio/RISE/archive/master.tar.gz && \  
tar xvzf *.gz && cd *master && \  
python setup.py install && \  
rm -f master.tar.gz  
WORKDIR /data  
  
# Lectures repo  
ENV branch bologna-mpi  
RUN git clone https://github.com/cineca-scai/lectures.git \  
&& cd lectures && git checkout $branch  
WORKDIR /data/lectures/nbcontent  

