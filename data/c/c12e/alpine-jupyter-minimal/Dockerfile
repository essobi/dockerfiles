FROM continuumio/miniconda  
  
RUN apt-get update  
RUN apt-get -y install \  
build-essential \  
libgsl0ldbl \  
gsl-bin \  
libgsl0-dev \  
libblas-dev \  
liblapack-dev \  
libatlas-base-dev \  
gfortran \  
cmake \  
vim \  
libarmadillo-dev \  
ca-certificates  
RUN conda config --set ssl_verify false  
RUN conda update conda  
RUN conda install jupyter -y --quiet \  
&& mkdir /opt/notebooks  
RUN conda install pip pandas scipy matplotlib seaborn pymongo ipython scikit-
learn opencv nltk gensim  
##### this has to be configured for each new environment ######  
EXPOSE 8888  
CMD /opt/conda/bin/jupyter notebook --ip='*' \--port=8888 \--no-browser  
#################################  

