FROM continuumio/anaconda3:latest  
  
ENV JUPYTER_CONFIG_DIR="/opt/jupyterconfig"  
RUN conda update -n base conda  
RUN conda install -c conda-forge jupyterlab  
RUN pip install SchemDraw  
RUN pip install control  
  
EXPOSE 9999  
CMD jupyter lab --ip=* --port 9999 --no-browser --allow-root --notebook-
dir=/opt/notebooks  

