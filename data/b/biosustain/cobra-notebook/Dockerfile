FROM jupyter/scipy-notebook:latest  
USER root  
RUN apt-get -y update && apt-get install -y swig libzmq3-dev libgmp-dev
libglpk-dev glpk-utils \  
pandoc python-dev python-pip libxml2 libxml2-dev zlib1g zlib1g-dev bzip2
libbz2-dev libxslt1-dev openbabel  
  
COPY requirements.txt requirements.txt  
  
# For Python 3.5 (default)  
RUN conda install -y scipy numpy pandas numexpr matplotlib  
RUN pip install pip --upgrade  
RUN pip install -r requirements.txt  
RUN python -c "from matplotlib import pyplot" # build font caches  
  
# For Python 3.4  
RUN conda create -y -n python3.4 python=3.4 scipy numpy pandas numexpr
matplotlib  
RUN /opt/conda/envs/python3.4/bin/pip install pip --upgrade  
RUN /opt/conda/envs/python3.4/bin/pip install -r requirements.txt  
RUN python -c "from matplotlib import pyplot" # build font caches  
  
RUN pip uninstall -y bokeh  
RUN /opt/conda/envs/python3.4/bin/pip uninstall -y bokeh  
  
ADD templates/ /srv/templates/  
RUN chmod a+rX /srv/templates  
RUN jupyter nbextension enable \--py widgetsnbextension  
  
USER jovyan  
ADD cameo-notebooks/ /home/jovyan/work/notebooks  
WORKDIR /home/jovyan/work/notebooks  
RUN for file in *.ipynb; do jupyter trust $file; done  
  
CMD jupyter notebook

