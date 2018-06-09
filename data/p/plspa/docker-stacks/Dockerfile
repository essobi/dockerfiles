# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM jupyter/all-spark-notebook  
  
MAINTAINER Jupyter Project <jupyter@googlegroups.com>  
  
#USER $NB_USER  
USER root  
  
# Update package management tool first  
RUN apt-get update  
  
# for SSML package  
RUN conda install --quiet --yes -c conda-forge jupyter_contrib_nbextensions  
RUN pip --no-cache-dir install
https://pypi.python.org/packages/81/c0/3c4e7b93aa4ef1edfde557065991c5f460cca54981fd562652bd80054612/pyssml-0.1.3.tar.gz  
  
# for DB packages  
RUN apt-get install -y freetds-dev  
RUN pip --no-cache-dir install pymssql  
  
#USER root  
WORKDIR $HOME  
VOLUME $HOME/work  
  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook-pa.sh"]  
  
COPY start-notebook-pa.sh /usr/local/bin/  
RUN chown -R $NB_USER:users /usr/local/bin/  
RUN chmod 755 /usr/local/bin/start-notebook-pa.sh  
  
USER $NB_USER  

