# Copyright (c) Jupyter Development Team.  
# This is a fork of the notebooks from Jupyter Dev Team.  
# Distributed under the terms of the Modified BSD License.  
FROM marcsaric/minimal-notebook  
  
LABEL maintainer="Marc Saric <marc.saric@gmx.de>"  
  
USER root  
  
# Testinstall the bash-kernel from https://github.com/takluyver/bash_kernel  
RUN pip install bash_kernel \  
&& python -m bash_kernel.install  
  
# Install all OS dependencies for fully functional notebook server  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
less \  
apt-utils \  
zlib1g-dev \  
liblzo2-dev \  
python2.7 \  
python-setuptools \  
python-pip \  
build-essential \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH=/usr/bin:$PATH  
  
RUN pip install pysam==0.13  
RUN pip install CrossMap==0.2.7  
  
ENV PATH=$CONDA_DIR/bin:$PATH \  
HOME=/home/$NB_USER  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_UID  

