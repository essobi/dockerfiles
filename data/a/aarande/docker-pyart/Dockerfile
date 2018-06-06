FROM continuumio/miniconda3  
MAINTAINER Aaron Anderson  
  
RUN groupadd -r pyart && useradd --no-log-init -ms /bin/bash -r -g pyart pyart  
RUN apt-get update && apt-get install -y gcc git libgl1-mesa-glx && apt-get
clean  
RUN conda config --append channels conda-forge &&\  
conda config --append channels http://conda.anaconda.org/jjhelmus && \  
conda install --yes numpy scipy xarray jupyter matplotlib netcdf4 pyproj
basemap nose pillow owslib pyepsg cartopy \  
trmm_rsl wradlib arm_pyart && pip install nexradaws && conda clean --all  
  
EXPOSE 8888  
RUN mkdir /opt/notebooks /opt/radar /opt/source && chown pyart:pyart
/opt/notebooks && chown pyart:pyart /opt/radar && chown pyart:pyart
/opt/source  
VOLUME /opt/notebooks /opt/radar /opt/source  
USER pyart  
WORKDIR /opt/source  
CMD ["python"]

