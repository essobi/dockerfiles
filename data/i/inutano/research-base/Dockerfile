# supercool docker image for reproducible data science  
# copyright: Tazro Inutano Ohta  
# Distributed under MIT License  
# version 0.1.1  
FROM debian:jessie  
  
MAINTAINER Tazro Inutano Ohta <inutano@gmail.com>  
  
USER root  
  
# Install prerequisites  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
git \  
nano \  
vim \  
wget \  
build-essential \  
python-dev \  
ca-certificates \  
bzip2 \  
unzip \  
sudo \  
locales \  
gfortran \  
gcc \  
libnettle4 \  
#libsm6 \  
#julia \  
#pandoc \  
#texlive-latex-base \  
#texlive-latex-extra \  
#texlive-fonts-extra \  
#texlive-fonts-recommended \  
#texlive-generic-recommended \  
#libxrender1 \  
#fonts-dejavu \  
&& apt-get clean  
  
# Setting locale  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen  
  
# Install tini  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc
/tini.asc  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 0527A9B7 \  
&& gpg --verify /tini.asc  
RUN chmod +x /tini  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Create user 'nijntje' with uid=1000 and in the 'users' group  
ENV CONTAINER_USER nijntje  
ENV NB_UID 1000  
RUN useradd -m -s /bin/bash -N -u $NB_UID $CONTAINER_USER && \  
mkdir -p /opt/conda && \  
chown nijntje /opt/conda  
  
# Setup home directory  
RUN mkdir /home/$CONTAINER_USER/work && \  
mkdir /home/$CONTAINER_USER/.jupyter && \  
mkdir /home/$CONTAINER_USER/.local  
  
# Nijntje, ook bekend als nijntje pluis, is de hoofdpersoon van een serie
kinderprentenboeken over een konijntje.  
USER nijntje  
  
# Install conda as nijntje  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-3.9.1-Linux-x86_64.sh && \  
echo "6c6b44acdd0bc4229377ee10d52c8ac6160c336d9cdd669db7371aa9344e1ac3
*Miniconda3-3.9.1-Linux-x86_64.sh" | sha256sum -c - && \  
/bin/bash Miniconda3-3.9.1-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda3-3.9.1-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda install --yes conda==3.14.1  
  
# Install Python 3 packages  
RUN conda install --yes \  
'pandas=0.17*' \  
'matplotlib=1.4*' \  
'numpy=1.10*' \  
'scipy=0.16*' \  
'seaborn=0.6*' \  
'scikit-learn=0.16*' \  
'scikit-image=0.11*' \  
'sympy=0.7*' \  
'cython=0.22*' \  
'patsy=0.4*' \  
'statsmodels=0.6*' \  
'cloudpickle=0.1*' \  
'dill=0.2*' \  
'numba=0.22*' \  
#'ipywidgets=4.0*' \  
#'bokeh=0.10*' \  
&& conda clean -yt  
  
# R packages including IRKernel which gets installed globally.  
RUN conda config --add channels r  
RUN conda install --yes \  
'rpy2=2.7*' \  
'r-base=3.2*' \  
'r-irkernel=0.5*' \  
'r-plyr=1.8*' \  
'r-devtools=1.9*' \  
'r-dplyr=0.4*' \  
'r-ggplot2=1.0*' \  
'r-tidyr=0.3*' \  
'r-rmarkdown=0.8*' \  
'r-forecast=5.8*' \  
'r-stringr=0.6*' \  
'r-rsqlite=1.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.1*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
#'r-shiny=0.12*' \  
'r-randomforest=4.6*' && conda clean -yt  
  
# switch to python 3.4.3  
RUN conda install --yes python==3.4.3  
  
# Switch user to root again  
USER root  
  
# Configure container startup as root  
ENTRYPOINT ["/tini", "--"]  
CMD ["bash"]  
  
# Configure working directory  
WORKDIR /home/$CONTAINER_USER/work  
RUN chown -R $CONTAINER_USER:users /home/$CONTAINER_USER  
  
# Hello, nijntje!  
USER nijntje  

