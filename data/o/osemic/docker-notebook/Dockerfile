FROM jupyter/datascience-notebook  
  
USER root  
  
# Update conda packages  
RUN conda update \--all \--no-channel-priority --yes && conda install tqdm
plotly xlwt xlsxwriter -c conda-forge -y  
  
# XGBoost  
RUN conda install -y gcc && \  
cd /usr/local/src && mkdir xgboost && cd xgboost && \  
git clone --recursive https://github.com/dmlc/xgboost.git && \  
cd xgboost && \  
make && cd python-package && python setup.py install && cd -  
  
# TensorFlow  
RUN pip3 install
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.0rc0-cp35-cp35m-linux_x86_64.whl  
  
# Upgrade to C++-based protobuf for TensorFlow  
RUN apt-get update && apt-get install -y autoconf automake libtool make g++
unzip && \  
git clone https://github.com/google/protobuf.git && \  
cd protobuf && ./autogen.sh && \  
CXXFLAGS="-fPIC -g -O2" ./configure && \  
make -j12 && export PROTOC=$PWD/src/protoc && \  
cd python && python setup.py bdist_wheel --cpp_implementation
--compile_static_extension && \  
pip3 uninstall -y protobuf && yes | pip3 install dist/*.whl && cd ../../  
  
USER $NB_USER  

