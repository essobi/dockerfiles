FROM jupyter/scipy-notebook  
  
USER root  
  
RUN apt-get update -y && \  
apt-get install -y sqlite3 libopencv-dev python-matplotlib && \  
# install a package into the default (python 3.x) environment  
conda install cartopy metpy netcdf4 gdal siphon xarray && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN bash -c "source activate python2; conda install opencv -y" && \  
cd / && git clone https://github.com/danforthcenter/plantcv.git && \  
cd /plantcv && \  
bash -c "source activate python2; python setup.py install"  
  
USER $NB_USER  
COPY start-notebook.sh /usr/local/bin/  
  
CMD ["start-notebook.sh", "--NotebookApp.token=''"]  

