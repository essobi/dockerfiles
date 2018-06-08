# from https://github.com/jupyter/docker-stacks/blob/master/scipy-
notebook/Dockerfile  
FROM jupyter/scipy-notebook  
  
# install some extra python libraries  
RUN conda install --quiet --yes \  
'tqdm' \  
'yapf' \  
'fire' \  
'lightgbm'  
  
# install notebook extensions  
RUN conda install --quiet --yes \  
jupyter_contrib_nbextensions && \  
jupyter nbextension enable collapsible_headings/main && \  
jupyter nbextension enable spellchecker/main  
  

