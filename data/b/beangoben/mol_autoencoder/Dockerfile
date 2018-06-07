FROM beangoben/pimp_jupyter  
  
USER root  
RUN ln -snf /bin/bash /bin/sh  
RUN apt-get update && \  
apt-get install -y gfortran liblapacke-dev liblapack-dev \  
libatlas-dev libpng12-dev libfreetype6-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER jovyan  
RUN conda update -n python2 matplotlib scipy numpy seaborn --quiet --yes && \  
conda clean --all  
RUN conda install -n python2 -c rdkit rdkit -y -q && \  
conda install -n python2 pandas=0.19 -y -q && \  
conda clean --all  
ADD requirements.txt /home/jovyan/work  
# chemio-informatics  
RUN source activate python2 && pip install --no-cache -r requirements.txt &&
rm requirements.txt  
# change default enviroment to python2  
RUN echo 'export PATH="/opt/conda/envs/python2/bin:$PATH"' >> ~/.bashrc  
  

