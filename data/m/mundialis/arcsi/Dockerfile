FROM continuumio/miniconda3:latest  
MAINTAINER Angelos Tzotsos <gcpp.kalxas@gmail.com>  
  
# update conda and install arcsi using conda package manager and clean up (rm
tar packages to save space)  
RUN conda update -n base conda  
RUN conda config \--add channels conda-forge && \  
conda config \--add channels au-eoed && \  
conda update --yes conda && \  
conda install --yes python=3.5 arcsi && \  
conda clean --yes -t  
  
# Ugly fixes for dependency versions  
RUN cd /opt/conda/lib && \  
ln -s libgeos-3.5.1.so libgeos-3.5.0.so && \  
ln -s libjpeg.so.9 libjpeg.so.8  
  
# set gdal paths  
ENV GDAL_DRIVER_PATH /opt/conda/lib/gdalplugins:$GDAL_DRIVER_PATH  
ENV GDAL_DATA /opt/conda/share/gdal  
  
# add debian packages required by arcsi  
RUN apt-get update && apt-get install -y libgfortran3 libglib2.0-0 libsm6
libxrender1 libfontconfig1 libxext6 libopenblas-base libgl1-mesa-glx  

