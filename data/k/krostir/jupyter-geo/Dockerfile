FROM jupyter/scipy-notebook  
  
LABEL maintainer="Kristof Ostir"  
  
# Install GDAL, rasterio, folium  
RUN conda install --quiet --yes \  
'gdal' \  
'rasterio' && \  
conda install -c conda-forge folium --quiet --yes && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  

