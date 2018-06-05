FROM phusion/baseimage:0.10.0  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
ENV KILL_PROCESS_TIMEOUT 30  
ENV KILL_ALL_PROCESSES_TIMEOUT 30  
MAINTAINER Kyle Wilcox <kyle@axiomdatascience.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y \  
binutils \  
build-essential \  
bzip2 \  
ca-certificates \  
file \  
libglib2.0-0 \  
libsm6 \  
libxext6 \  
libxrender1 \  
pwgen \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup CONDA (https://hub.docker.com/r/continuumio/miniconda3/~/dockerfile/)  
ENV MINICONDA_VERSION latest  
ENV PYTHON_VERSION 3.6  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
curl -k -o /miniconda.sh
https://repo.continuum.io/miniconda/Miniconda3-$MINICONDA_VERSION-
Linux-x86_64.sh && \  
/bin/bash /miniconda.sh -b -p /opt/conda && \  
rm /miniconda.sh && \  
/opt/conda/bin/conda config \  
\--set always_yes yes \  
\--set changeps1 no \  
\--set show_channel_urls True \  
&& \  
/opt/conda/bin/conda config \  
\--add create_default_packages pip \  
\--add channels axiom-data-science \  
\--add channels conda-forge \  
&& \  
/opt/conda/bin/conda install python=$PYTHON_VERSION && \  
/opt/conda/bin/conda clean -a -y  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Install requirements  
COPY requirements*.txt /tmp/  
RUN conda install -y \  
\--file /tmp/requirements.txt \  
&& \  
conda clean -a -y  
  
ENV GUTILS_BINARY_DIRECTORY /gutils/binary  
VOLUME $GUTILS_BINARY_DIRECTORY  
  
ENV GUTILS_ASCII_DIRECTORY /gutils/ascii  
VOLUME $GUTILS_ASCII_DIRECTORY  
  
ENV GUTILS_NETCDF_DIRECTORY /gutils/netcdf  
VOLUME $GUTILS_NETCDF_DIRECTORY  
  
ENV GUTILS_CONFIG_DIRECTORY /gutils/config  
VOLUME $GUTILS_CONFIG_DIRECTORY  
  
ENV GUTILS_ERDDAP_CONTENT_PATH /gutils/erddap/content  
VOLUME $GUTILS_ERDDAP_CONTENT_PATH  
  
ENV GUTILS_ERDDAP_FLAG_PATH /gutils/erddap/flag  
VOLUME $GUTILS_ERDDAP_FLAG_PATH  
  
RUN mkdir -p /etc/my_init.d && \  
mkdir -p /gutils  
COPY docker/init/* /etc/my_init.d/  
  
ENV GUTILS_VERSION 2.7.0  
ENV PROJECT_ROOT /code  
RUN mkdir -p "$PROJECT_ROOT"  
COPY . $PROJECT_ROOT  
WORKDIR $PROJECT_ROOT  
RUN pip install .  

