FROM duartej/eudaqv1-ubuntu:eutelescope  
LABEL author="jorge.duarte.campderros@cern.ch" \  
version="0.1-alpha" \  
description="Docker image to integrate the RD53A chip \  
using the bdaq53 readout system into EUDAQ"  
  
# Be sure running as root  
USER 0  
  
# Place at the directory  
WORKDIR /bdaq53  
  
# Install all dependencies  
RUN apt-get update \  
&& apt-get -y install \  
python-pip \  
python-yaml \  
python-requests \  
python-pyqt5 \  
python-tk \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download minicoda (and recovering permissions)  
RUN mkdir -p /bdaq53 \  
&& wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
-O /bdaq53/miniconda2.sh \  
&& chown -R eudaquser:eudaquser /bdaq53 \  
&& chown -R eudaquser:eudaquser /eudaq  
  
# Change to user and conda installation  
USER eudaquser  
ENV HOME="/home/eudaquser"  
ENV PATH="${PATH}:${HOME}/.local/bin:/bdaq53/miniconda/bin"  
ENV PYTHONPATH="${HOME}/.local/lib:${PYTHONPATH}:/bdaq53/miniconda"  
RUN cd /bdaq53 \  
&& /bin/bash miniconda2.sh -b -p /bdaq53/miniconda \  
&& . activate \  
&& conda update -y -n base conda \  
&& conda install -y \  
numpy \  
bitarray \  
pyyaml \  
scipy \  
numba \  
pytables \  
matplotlib \  
tqdm \  
pyzmq \  
blosc \  
psutil \  
cython \  
&& pip install --upgrade pip  
# Not exist anymore, merged to development  
#RUN pip install --user
git+https://gitlab.cern.ch/silab/bdaq53.git@development  
RUN . /bdaq53/miniconda/bin/activate \  
&& git clone -b development https://gitlab.cern.ch/silab/bdaq53.git \  
&& cd bdaq53 \  
&& pip install -e . --user  
  
# Activate conda environment and (re-)install the bdaq53 direcotory  
# (case of bind-volumen mounted)  
ENTRYPOINT ["/bin/bash", "-c","source /bdaq53/miniconda/bin/activate \  
&& cd /bdaq53/bdaq53 && export PYTHONPATH=$PYTHONPATH:/bdaq53/bdaq53 \  
&& pip install -e . && /bin/bash"]  

