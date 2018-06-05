FROM phusion/baseimage:0.9.21  
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
ENV MINICONDA_VERSION 4.2.12  
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
\--add channels conda-forge \  
\--add channels axiom-data-science \  
&& \  
/opt/conda/bin/conda clean -a -y  
  
ENV PATH /opt/conda/bin:$PATH  
  
# Install requirements  
COPY requirements*.txt /tmp/  
RUN conda install -y \  
\--file /tmp/requirements.txt \  
&& \  
conda clean -a -y  
  
RUN mkdir -p /etc/my_init.d  
COPY docker/init/* /etc/my_init.d/  
  
ENV GDB_DATA_DIR /data  
VOLUME $GDB_DATA_DIR  
  
ENV GDAM2NC_OUTPUT /output  
VOLUME $GDAM2NC_OUTPUT  
  
ENV GDAM2NC_CONFIG /config  
VOLUME $GDAM2NC_CONFIG  
  
EXPOSE 44444  
ENV GDAM_VERSION 1.2.3  
ENV PROJECT_ROOT /code  
RUN mkdir -p "$PROJECT_ROOT"  
COPY . $PROJECT_ROOT  
WORKDIR $PROJECT_ROOT  
RUN pip install .  

