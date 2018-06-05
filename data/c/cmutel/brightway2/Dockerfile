FROM jupyter/minimal-notebook  
  
# Some stuff from https://github.com/jupyter/docker-stacks/blob/master/scipy-
notebook/Dockerfile  
MAINTAINER Chris Mutel <cmutel@gmail.com>  
  
USER root  
  
# libav-tools for matplotlib anim  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libav-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
# Install Python packages  
RUN conda install --quiet --yes wheel && \  
conda update --yes pip wheel setuptools && \  
conda install -y -q -c conda-forge -c cmutel -c haasad brightway2 jupyter
pypardiso jupyter_contrib_nbextensions jupyter_nbextensions_configurator
pandas seaborn scikit-learn fiona rasterio rtree pillow shapely && \  
pip install --user --no-cache-dir
https://bitbucket.org/cmutel/brightway2-regional/get/tip.zip#egg=bw2regional-0.3
&& \  
conda clean -tipsy  
  
# Import matplotlib the first time to build the font cache.  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"  
  
# Configure ipython kernel to use matplotlib inline backend by default  
RUN mkdir -p $HOME/.ipython/profile_default/startup  
COPY mplimporthook.py $HOME/.ipython/profile_default/startup/  
  
RUN mkdir /home/jovyan/data  
RUN mkdir /home/jovyan/notebooks  
RUN mkdir /home/jovyan/output  
  
ENV BRIGHTWAY2_DOCKER 1  
ENV BRIGHTWAY2_DIR /home/jovyan/data  
ENV BRIGHTWAY2_OUTPUT_DIR /home/jovyan/output  
  
WORKDIR /home/jovyan/notebooks  

