FROM jupyter/datascience-notebook  
MAINTAINER Shigeru Kitazaki <skitazaki@gmail.com>  
  
USER jovyan  
  
RUN conda install --yes --quiet \  
'psycopg2=2.6*' \  
&& conda install --yes --quiet -c sodre 'ipython-sql=0.3*' \  
&& conda clean -tipsy  

