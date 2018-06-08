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
RUN apt-get update && apt-get install -y --no-install-recommends \  
libpng3 libfreetype6-dev libatlas-base-dev gfortran \  
libgdal1-dev libjpeg-dev sasl2-bin libsasl2-2 libsasl2-dev \  
libsasl2-modules unixodbc-dev python3-tk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install python2 libraries  
RUN pip2 --no-cache-dir install \  
beautifulsoup4==4.5.3 \  
bokeh==0.12.13 \  
Cython==0.27.3 \  
dask==0.16.0 \  
fiona==1.7.11 \  
folium==0.4.0 \  
fastavro==0.17.7 \  
h5py==2.7.1 \  
hdfs==2.0.16 \  
ibis-framework==0.12.0 \  
impyla==0.14.0 \  
ipywidgets==7.0.5 \  
matplotlib==2.1.1 \  
mpld3==0.3 \  
numba==0.31.0 \  
numpy==1.14.0 \  
networkx==2.0 \  
pandas==0.21.1 \  
Pillow==5.0.0 \  
pybrain==0.3 \  
pymongo==3.2.2 \  
pyodbc==4.0.21 \  
requests-kerberos==0.12.0 \  
sasl==0.2.1 \  
scikit-image==0.13.1 \  
scikit-learn==0.19.1 \  
scipy==1.0.0 \  
seaborn==0.8.1 \  
shapely==1.6.3 \  
SQLAlchemy==1.1.13 \  
statsmodels==0.8.0 \  
thrift_sasl==0.2.1 \  
vega==0.4.4 \  
vincent==0.4.4 && \  
rm -rf /root/.cachex  
  
USER $NB_USER  
  
# Add libraries and upgrade libraries installed in base image for python 3  
RUN conda install --quiet --yes \  
'fiona=1.7.11' \  
'folium=0.4.0' \  
'hdf5=1.10.1' \  
'python-hdfs=2.0.16' \  
'ibis-framework=0.12.0' \  
'impyla=0.14.0' \  
'matplotlib=2.1.1' \  
'mpld3=0.3' \  
'networkx=2.0' \  
'numpy=1.14.2' \  
'pandas=0.21.1' \  
'pillow=4.3.0' \  
'pymongo=3.2.2' \  
'pyodbc=4.0.21' \  
'sasl=0.2.1' \  
'scikit-image=0.13.1' \  
'scikit-learn=0.19.1' \  
'scipy=1.1.0' \  
'shapely=1.6.3' \  
'seaborn=0.8.1' \  
'SQLAlchemy=1.1.13' \  
'thrift_sasl=0.2.1' && \  
conda remove --quiet --yes \--force qt pyqt && \  
conda clean -tipsy && \  
npm cache clean && \  
rm -rf $CONDA_DIR/share/jupyter/lab/staging && \  
fix-permissions $CONDA_DIR  
  
  
##### PM 128 ####  
  
RUN conda install --quiet --yes \  
'lxml=4.2.1' \  
'tabula-py=1.1.1' \  
'tika=1.16' \  
'xlwt=1.3.0' \  
'nltk=3.2.5' \  
'python-Levenshtein=0.12.0' \  
'joblib=0.11' \  
'django=2.0.5' \  
'Jellyfish=0.6.1' \  
'Openpyxl=2.5.3' \  
'tensorflow=1.8.0' \  
'keras=2.1.5' \  
'scrapy=1.5.0' \  
'simplejson=3.15.0' \  
'pycurl=7.43.0.1' \  
'elasticsearch=6.2.0' \  
'fastparquet=0.1.5' \  
'spacy=2.0.11' \  
'pycrypto=2.6.1' && \  
conda remove --quiet --yes \--force qt pyqt && \  
conda clean -tipsy && \  
npm cache clean && \  
rm -rf $CONDA_DIR/share/jupyter/lab/staging && \  
fix-permissions $CONDA_DIR  
  
USER root  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \  
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig redis-server
libpulse-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install pip3  
RUN cd /tmp && wget https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py  
  
RUN pip3 --no-cache-dir install \  
textract==1.6.1 \  
excel==1.0.0 \  
tokenizer==1.0.3 \  
apiclient==1.0.3 \  
crypto==1.4.1 \  
addok==1.0.2 \  
neo4j-driver==1.6.0 && \  
rm -rf /root/.cachex  
  
RUN pip2 --no-cache-dir install \  
lxml==4.2.1 \  
xlwt==1.3.0 \  
nltk==3.3 \  
openpyxl==2.5.3 \  
python-levenshtein==0.12.0 \  
joblib==0.11 \  
simplejson==3.15.0 \  
jellyfish==0.6.1 \  
tokenizer==1.0.3 \  
apiclient==1.0.3 \  
elasticsearch==6.2.0 \  
graphviz==0.8.3 \  
pycrypto==2.6.1 \  
crypto==1.4.1 \  
tabula-py==1.2.0 \  
textract==1.6.1 \  
tika==1.16 \  
scrapy==1.5.0 \  
tensorflow==1.8.0 \  
keras==2.1.6 \  
django==1.11.13 \  
gensim==3.4.0 \  
spacy==2.0.11 \  
excel==1.0.0 \  
Cython==0.28.3 \  
numba==0.38 \  
fastparquet==0.1.5 \  
addok==1.0.2 \  
neo4j-driver==1.6.0 &&\  
rm -rf /root/.cachex  
  
##### END PM 128 ####  
# Create default workdir (useful if no volume mounted)  
RUN mkdir /notebooks-dir && chown 1000:100 /notebooks-dir  
# Add permission on /usr/local/lib/python2.7/ to allow Jovyan to 'pip2
install'  
RUN chown -R $NB_USER:users /usr/local/lib/python2.7/  
USER $NB_USER  
  
# Fix kernel config  
RUN python2 -m ipykernel install --user  
  
# Define default workdir  
WORKDIR /notebooks-dir  
  
# Install Saagie plugin  
USER root  
RUN pip --no-cache-dir install jupyter-saagie-plugin==1.0.6  
  
USER $NB_USER  
  
# Default: run without authentication  
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--
NotebookApp.password=''"]  

