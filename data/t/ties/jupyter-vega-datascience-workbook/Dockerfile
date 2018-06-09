FROM jupyter/datascience-notebook  
  
# Update conda first to fix IsADirectoryError  
RUN conda install -n base conda && \  
conda install -c anaconda networkx && \  
conda install -c anaconda psycopg2 && \  
conda install -c conda-forge altair && \  
conda install -c conda-forge ipyleaflet && \  
conda install -c conda-forge ipython-sql && \  
conda install -c conda-forge elasticsearch && \  
conda install -c conda-forge elasticsearch-dsl && \  
conda install -c conda-forge neo4j-python-driver && \  
conda install -c damianavila82 rise && \  
conda install seaborn && \  
pip install nx_altair && \  
jupyter labextension install @jupyterlab/vega3-extension && \  
jupyter labextension install jupyter-leaflet && \  
jupyter labextension install @jupyter-widgets/jupyterlab-manager  
  
# Add the examples  
USER jovyan  
ADD examples /home/jovyan/examples  

