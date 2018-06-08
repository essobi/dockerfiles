FROM jupyter/scipy-notebook:c7fb6660d096  
  
MAINTAINER Saagie  
  
# Add python 2 kernel  
RUN conda create -n ipykernel_py2 python=2 ipykernel --yes  
RUN /bin/bash -c "source activate ipykernel_py2"  
RUN python -m ipykernel install --user  
  
USER root  
  
# Install pip2  
RUN cd /tmp && wget https://bootstrap.pypa.io/get-pip.py && \  
python2 get-pip.py  
  
# Install libraries dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends python-numpy
\  
python3-numpy libpng3 libfreetype6-dev libatlas-base-dev gfortran \  
libgdal1-dev libjpeg-dev sasl2-bin libsasl2-2 libsasl2-dev \  
libsasl2-modules unixodbc-dev python3-tk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install python2 libraries  
RUN pip2 --no-cache-dir install \  
bokeh==0.12.13 \  
fiona==1.7.11 \  
folium==0.4.0 \  
hdfs[avro,dataframe,kerberos] \  
ibis-framework==0.12.0 \  
impyla==0.14.0 \  
ipywidgets==7.0.5 \  
matplotlib==2.1.1 \  
mpld3==0.3 \  
networkx==2.0 \  
pandas==0.21.1 \  
pybrain==0.3 \  
pymongo==3.2.2 \  
pyodbc==4.0.21 \  
sasl==0.2.1 \  
scikit-image==0.13.1 \  
scikit-learn==0.19.1 \  
scipy==1.0.0 \  
seaborn==0.8.1 \  
shapely==1.6.3 \  
SQLAlchemy==1.1.13 \  
statsmodels==0.8.0 \  
thrift_sasl==0.3.0 && \  
rm -rf /root/.cachex  
  
USER $NB_USER  
  
# Add libraries and upgrade libraries installed in base image for python 3  
RUN conda install --quiet --yes \  
'fiona=1.7.11' \  
'folium=0.4.0' \  
'hdf5=1.10.1' \  
'ibis-framework=0.12.0' \  
'impyla=0.14.0' \  
'matplotlib=2.1.1' \  
'mpld3=0.3' \  
'networkx=2.0' \  
'pandas=0.21.1' \  
'pymongo=3.2.2' \  
'pyodbc=4.0.21' \  
'sasl=0.2.1' \  
'scikit-image=0.13.1' \  
'scikit-learn=0.19.1' \  
'scipy=1.0.0' \  
'shapely=1.6.3' \  
'seaborn=0.8.1' \  
'SQLAlchemy=1.1.13' \  
'thrift_sasl=0.3.0' && \  
conda remove --quiet --yes \--force qt pyqt && \  
conda clean -tipsy && \  
npm cache clean && \  
rm -rf $CONDA_DIR/share/jupyter/lab/staging && \  
fix-permissions $CONDA_DIR  
  
# Create default workdir (useful if no volume mounted)  
USER root  
RUN mkdir /notebooks-dir && chown 1000:100 /notebooks-dir  
USER $NB_USER  
  
# Define default workdir  
WORKDIR /notebooks-dir  
  
# Default: run without authentication  
CMD ["start-notebook.sh", "--NotebookApp.token=''"]  

