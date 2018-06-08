FROM jupyter/pyspark-notebook  
MAINTAINER Freaxmind  
  
USER root  
RUN conda install -y pymongo nbgrader  
  
USER $NB_USER  
WORKDIR $HOME/work  
CMD start-notebook.sh --NotebookApp.token=\"\"  

