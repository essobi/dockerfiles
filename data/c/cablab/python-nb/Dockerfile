From jupyter/base-notebook:8f56e3c47fec  
LABEL maintainer="Brockmann Consult GmbH <http://www.brockmann-consult.de>"  
  
ADD start.sh /usr/local/bin/start.sh  
  
USER root  
RUN sudo apt-get update  
RUN sudo apt-get install -y git  
  
USER $NB_USER  
  
# Install python modules  
RUN conda install --quiet --yes -c conda-forge -c cablab -c anaconda -c numba
\  
nomkl \  
ipywidgets=7.0* \  
pandas \  
numexpr \  
matplotlib=2.0* \  
scipy \  
seaborn \  
scikit-learn \  
scikit-image \  
cython=0.25* \  
numba=0.34* \  
bokeh \  
hdf5 \  
h5py \  
xarray \  
dask \  
gridtools \  
basemap=1.0.7 \  
ffmpeg=2.8.6 \  
netcdf4=1.2*  
  
# Activate ipywidgets extension in the environment that runs the notebook
server  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
# Import matplotlib the first time to build the font cache.  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"  
  
USER root  
  
# Install cablab  
WORKDIR /srv/jupyterhub  
RUN git clone https://github.com/CAB-LAB/cablab-core.git  
WORKDIR /srv/jupyterhub/cablab-core  
RUN python setup.py install  
  
USER $NB_USER  
WORKDIR /home/jovyan/work

