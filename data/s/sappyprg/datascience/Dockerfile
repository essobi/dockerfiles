FROM continuumio/anaconda3  
  
MAINTAINER Dan Lim <imdanboy@gmail.com>  
  
RUN apt-get update && apt-get install -y build-essential  
  
# install jupyter notebook & notebook directory  
RUN /opt/conda/bin/conda install jupyter -y  
RUN mkdir /notebooks  
  
# install xgboost  
RUN git clone \--recursive https://github.com/dmlc/xgboost  
# install xgboost of python package (scikit-learn api)  
RUN cd xgboost; make -j4  
RUN cd xgboost/python-package; python setup.py install  
  
# install theano  
RUN pip install Theano  
  
# install tensorflow  
RUN conda install -c conda-forge tensorflow  
  
# install keras  
RUN pip install keras  

