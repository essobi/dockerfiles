FROM jupyter/datascience-notebook  
  
RUN conda install --quiet --yes -n python2 altair --channel conda-forge &&
conda clean -tipsy  
RUN conda install --quiet --yes -n python3 altair --channel conda-forge &&
conda clean -tipsy  

