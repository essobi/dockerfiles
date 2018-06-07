FROM jupyter/pyspark-notebook  
  
MAINTAINER Pierre Navaro <pierre.navaro@univ-rennes1.fr>  
  
USER root  
  
COPY . ${HOME}  
  
RUN chown -R ${NB_USER} ${HOME}  
  
USER $NB_USER  
  
RUN conda install --quiet --yes -c conda-forge \  
'lorem' 'dask' 'pandas' 'pytables' \  
'joblib' 'ujson' \  
'graphviz' 'python-graphviz' 'beautifulsoup4' \  
'toolz' 'h5py' 'partd' 'matplotlib' 'seaborn' \  
'hdfs3' 'progressbar2' 'pyarrow' \  
'feather-format' 'fastparquet' 'distributed' \  
'xlwt' 'fastparquet' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN pip install --no-cache-dir toyplot && \  
fix-permissions $CONDA_DIR  

