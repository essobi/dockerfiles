FROM jupyter/minimal-notebook  
  
MAINTAINER Evandro Dutra <evandro.eld@gmail.com>  
  
USER root  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
  
RUN apt-get update && apt-get install -yq \  
libav-tools \  
gcc && apt-get clean && cd ~ \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
RUN conda update --all && \  
conda install --quiet --yes \  
'nomkl' \  
'ipywidgets' \  
'pandas' \  
'numexpr' \  
'matplotlib' \  
'scipy' \  
'scikit-learn' \  
'scikit-image' \  
'sympy' \  
'patsy' \  
'statsmodels' \  
'dill' \  
'numba' \  
'bokeh' \  
'hdf5' \  
'h5py' \  
'vincent' \  
'protobuf' \  
'numpy' \  
'Pillow' \  
'psutil' \  
'tensorflow' \  
'seaborn' \  
'folium' \  
'xlrd' && \  
conda remove --quiet --yes \--force qt pyqt && \  
conda clean -tipsy && \  
jupyter nbextension enable --py widgetsnbextension --sys-prefix && \  
fix-permissions $CONDA_DIR  
  
RUN cd /tmp && \  
git clone https://github.com/PAIR-code/facets.git && \  
cd facets && \  
jupyter nbextension install facets-dist/ --sys-prefix && \  
rm -rf facets && \  
fix-permissions $CONDA_DIR  
  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \  
fix-permissions /home/$NB_USER  
  
USER $NB_USER  

