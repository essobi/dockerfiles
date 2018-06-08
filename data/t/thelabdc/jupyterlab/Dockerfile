FROM jupyter/datascience-notebook  
  
USER root  
RUN apt-get update && apt-get install -y openssh-client  
USER jovyan  
  
# Install JupyterLab  
RUN pip install jupyterlab && \  
jupyter serverextension enable \--py jupyterlab  
# Start JupyterLab  
CMD ["start.sh", "jupyter", "lab"]  

