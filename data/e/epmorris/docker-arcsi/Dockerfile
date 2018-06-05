FROM continuumio/miniconda:py34_latest  
MAINTAINER Edward P. Morris <edward.morris@uca.es>  
  
# update conda and install arcsi using conda package manager and clean up (rm
tar packages to save space)  
RUN conda update \--yes conda && \  
conda install --yes -c https://conda.binstar.org/osgeo arcsi && \  
conda clean -t  
  
# set gdal paths  
ENV GDAL_DRIVER_PATH /opt/anaconda/gdalplugins:$GDAL_DRIVER_PATH  
ENV GDAL_DATA /opt/anaconda/share/gdal  
  
# add debian packages required by arcsi  
RUN apt-get update && apt-get install -y libgfortran3 libglib2.0-0 libsm6
libxrender1 libfontconfig1 libxext6  
  

