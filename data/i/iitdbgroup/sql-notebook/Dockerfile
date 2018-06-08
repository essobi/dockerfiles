# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/minimal-notebook  
  
MAINTAINER Boris Glavic <bglavic@iit.edu>  
  
USER $NB_USER  
  
# Install SQL magic and postgres library  
RUN conda install --quiet --yes \  
'ipython-sql' \  
'psycopg2' \  
&& conda clean -tipsy  

