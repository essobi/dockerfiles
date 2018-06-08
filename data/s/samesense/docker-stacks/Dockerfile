# Copyright (c) Jupyter Development Team.  
FROM samesense/docker-stacks-minimal  
  
MAINTAINER Aaron J. Masino  
  
USER root  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libxrender1 \  
fonts-dejavu \  
gfortran \  
python-qt4 \  
gcc && apt-get clean  
  
USER choptiu  
  
RUN conda config --add channels r  
RUN conda install --yes \  
'r-base' \  
'r-irkernel' \  
'r-plyr' \  
'r-devtools' \  
'r-dplyr' \  
'r-ggplot2' \  
'r-tidyr' \  
'r-rmarkdown' \  
'r-forecast' \  
'r-stringr' \  
'r-rsqlite' \  
'r-reshape2' \  
'r-caret' \  
'r-rcurl' \  
'r-randomforest' && conda clean -yt  
  
# Install Python 3 packages  
RUN conda install --yes \  
'ipywidgets=4.0*' \  
'pandas' \  
'xlrd' \  
'matplotlib=1.5*' \  
'scipy=0.17*' \  
'seaborn=0.7*' \  
'scikit-learn' \  
'scikit-image' \  
'sympy=1.0*' \  
'cython=0.23*' \  
'patsy=0.4*' \  
'statsmodels=0.6*' \  
'cloudpickle=0.1*' \  
'dill=0.2*' \  
'numba=0.24*' \  
'bokeh=0.11*' \  
'nltk=3.2*' \  
'theano=0.7*' \  
'psycopg2=2.6*' \  
'sqlalchemy=1.0*' \  
'pymongo=3*' \  
'gensim=0.12*' \  
&& conda clean -yt  
  
RUN conda install --yes -c r rpy2  
  
RUN conda clean -yt  
  
RUN conda update --yes scikit-learn  
  
# Install Python 2 packages  
RUN conda create --yes -p $CONDA_DIR/envs/python2 python=2.7 \  
'ipython=4.0*' \  
'ipywidgets=4.0*' \  
'pandas' \  
'matplotlib' \  
'scipy' \  
'seaborn' \  
'scikit-learn' \  
'scikit-image' \  
'sympy' \  
'cython' \  
'patsy' \  
'statsmodels' \  
'cloudpickle' \  
'dill' \  
'numba' \  
'bokeh' \  
'nltk' \  
'psycopg2' \  
'sqlalchemy' \  
'theano' \  
'pymongo'\  
'gensim' \  
'pyzmq' \  
&& conda clean -yt  
  
RUN pip install -U mock nose arrow requests  
  
# RUN python -m nltk.downloader all  
  
USER root  
  
# Install Python 2 kernel spec globally to avoid permission problems when
NB_UID  
# switching at runtime.  
RUN $CONDA_DIR/envs/python2/bin/python \  
$CONDA_DIR/envs/python2/bin/ipython \  
kernelspec install-self  
  

