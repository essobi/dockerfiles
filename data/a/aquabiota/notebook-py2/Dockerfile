# -*- mode: ruby -*-  
# vi: set ft=ruby :  
# docker run -i -t -p 8888:8888 -v $(pwd):/home/aqua/workspace/notebooks
aquabiota/notebook-py2 jupyter notebook --ip='*' --port=8888 --no-browser  
# docker run -i -t -p 8888:8888 aquabiota/notebook-py2 jupyter notebook
--ip='*' --port=8888 --no-browser  
# MODIFIED FROM: https://github.com/ContinuumIO/docker-
images/blob/master/anaconda3/Dockerfile  
FROM aquabiota/notebook-base:latest  
  
LABEL maintainer "Aquabiota Solutions AB <mapcloud@aquabiota.se>"  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER $NB_USER  
# NOTE. this will install the full anaconda but for python 2. Only for
develop.  
# Packages for production can be added in a yaml env file.  
RUN conda create -y -n ipykernel_py2 python=2 ipykernel  
  
RUN ["/bin/bash", "-c", "source activate ipykernel_py2 && python -m ipykernel
install --user" ]  
#RUN ["/bin/bash", "-c", "source activate ipykernel_py2 && conda install --yes
-v anaconda"]  
# Preparing Nansat install  
# https://github.com/nansencenter/nansat  
ENV GDAL_DATA $CONDA_DIR/share/gdal/  
ENV GEOS_DIR $CONDA_DIR  
RUN conda install -n ipykernel_py2 -q --yes -c conda-forge numpy pandas \  
matplotlib nose pillow basemap netcdf4 gdal pyproj geopy rasterio \  
cmocean cartopy iris shapely yaml  
  
RUN conda install -n ipykernel_py2 -y bcrypt passlib  
  
RUN ["/bin/bash", "-c", "source activate ipykernel_py2 && pip install
pyorient"]  
RUN ["/bin/bash", "-c", "source activate ipykernel_py2 && pip install
https://github.com/nansencenter/nansat/archive/master.tar.gz"]  
  
# Make sure the user have access to the .local subfolder  
USER root  
RUN chown -R $NB_USER:users $HOME/.local  
  
# Ensure that container starts with the Notebook_user  
USER $NB_USER  

