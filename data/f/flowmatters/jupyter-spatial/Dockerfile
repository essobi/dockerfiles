FROM jupyter/datascience-notebook  
  
COPY requirements.txt /home/jovyan/requirements.txt  
  
USER jovyan  
  
RUN conda install -y -c conda-forge gdal && \  
pip install -r /home/jovyan/requirements.txt && \  
python -c "import osgeo.gdal" && \  
python -c "import pandas, geopandas"  
  
CMD start.sh jupyter lab \--port=22222  

