FROM vishnumohan/miniconda3  
  
MAINTAINER Vishnu Mohan <vishnu@mesosphere.com>  
  
COPY environment.yml "$CONDA_USER_HOME/work"  
RUN $CONDA_USER_HOME/conda/bin/conda env create --json -q -f environment.yml \  
&& $CONDA_USER_HOME/conda/bin/conda clean --json -tipsy  
  
EXPOSE 8888 8786 8787 9786  
CMD ["notebook.sh"]  
  
COPY jupyter_notebook_config.py "$CONDA_USER_HOME/.jupyter/"  
COPY notebook-home.sh "/usr/local/bin/notebook.sh"  
COPY start-dask-scheduler.sh /usr/local/bin/  
COPY start-dask-worker.sh /usr/local/bin  

