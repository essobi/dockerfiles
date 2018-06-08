ARG VER=0.9  
FROM jupyterhub/singleuser:$VER  
RUN pip install s3contents dask toolz  
RUN conda config \--system --prepend channels conda-forge && \  
conda config \--system --set auto_update_conda false && \  
conda config \--system --set show_channel_urls true && \  
conda install --quiet --yes jupyter notebook jupyterlab && \  
conda install --quiet --yes r r-irkernel && \  
conda clean -tipsy && \  
jupyter labextension install @jupyterlab/hub-extension && \  
npm cache clean --force  
  
COPY config/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py  

