FROM jupyter/all-spark-notebook  
MAINTAINER Khwunchai Jaengsawang <khwunchai.j@ku.th>  
  
USER root  
  
# Install gcc required for xgboost  
RUN conda install --yes --quiet gcc  
  
ENV PYTHONPATH $PYTHONPATH:/usr/local/src/xgboost/python-package  
  
# Install R packages  
RUN conda install --yes --quiet --channel r \  
r-essentials \  
r-devtools && \  
conda install --yes --quiet --channel bioconda \  
r-readr && \  
conda clean -tipsy  
  
# Install Python packages  
RUN conda install --yes --quiet --channel conda-forge \  
ggplot  
  
# Add live slideshows with RISE  
RUN wget https://github.com/damianavila/RISE/archive/master.tar.gz \  
&& tar xvzf *.gz && cd RISE-master && python3 setup.py install  
  
# Download, build and install xgboost for R and Python  
RUN cd /usr/local/src && \  
git clone \--recursive https://github.com/dmlc/xgboost && \  
cd /usr/local/src/xgboost && \  
make Rbuild && make -j4 && \  
R CMD INSTALL xgboost_*.tar.gz  
  
USER $NB_USER  

