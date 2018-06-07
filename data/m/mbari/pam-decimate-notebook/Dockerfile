FROM jupyter/base-notebook  
  
MAINTAINER Danelle Cline <dcline@mbari.org>  
  
USER root  
RUN apt-get -qq update && \  
apt-get install -y libsndfile1 && \  
apt-get install -y gcc && \  
apt-get install -y libatlas-base-dev  
  
# Uncomment to include PDF support (makes Docker images larger!)  
# apt-get install -y texlive-xetex pandoc  
USER $NB_UID  
  
RUN conda create --name decimate  
RUN /bin/bash -c "source activate decimate"  
  
# Install Python 3 packaes  
RUN conda install --quiet --yes \  
'matplotlib==2.2.2' \  
'pandas==0.22.0' \  
'scipy==1.0.1' \  
'cython=0.25*'  
  
# A few are not in the conda channels, so install with pip  
RUN pip install pydsm==0.13.0.1  
RUN pip install pysoundfile==0.9.0  
  
ADD work/decimate.ipynb .  
ADD work/test.wav .  
ADD work/tone1200Hz.wav .  

