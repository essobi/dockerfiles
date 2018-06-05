FROM jupyter/datascience-notebook:latest  
  
RUN conda install -y numpy  
RUN conda install -y -c cvxgrp cvxpy libgcc  
RUN conda install -y -c conda-forge tensorflow  
RUN conda install -c damianavila82 rise  
  
# the password is geneva18  
ADD ./config.json /home/jovyan/.jupyter/jupyter_notebook_config.json  
  
# copy the notebooks over  
USER root  
  
# make sure all files in the work folder are jovyan:users  
# make sure that they are on the host  
ADD ./books /home/jovyan/work  
RUN chgrp -R 100 /home/jovyan/work  
RUN chown -R 1000 /home/jovyan/work  
  
USER jovyan  
  
CMD start-notebook.sh  

