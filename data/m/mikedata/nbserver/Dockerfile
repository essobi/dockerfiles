FROM jupyter/minimal-notebook  
  
MAINTAINER Michael Adams (ONS Open Data Team)  
  
USER root  
  
USER $NB_USER  
  
# install databaker  
RUN pip install databaker  
  
# Install Python 3 packages  
# adapted from: https://github.com/jupyter/docker-stacks/blob/master/scipy-
notebook/Dockerfile  
RUN conda install --quiet --yes \  
'nomkl' \  
'ipywidgets=6.0*' \  
'pandas=0.19*' \  
'beautifulsoup4=4.5.*'  
# Add notebbok extensions (to enable hiding collapsing/hiding of cell content)
then enable hide  
# We're going via conda again as it includes html/javscript bits we'll need  
RUN conda install -c conda-forge jupyter_contrib_nbextensions  
RUN jupyter nbextension enable hide_input/main  
  
# Pull the notebooks in  
RUN git clone https://github.com/MikeData/beta_transformations_walkthrough  
  
# Activate ipywidgets extension in the environment that runs the notebook
server  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  

