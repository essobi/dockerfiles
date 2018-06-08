# Distributed under the terms of the Modified BSD License.  
# FROM jupyter/minimal-notebook  
FROM jupyter/datascience-notebook  
  
MAINTAINER Duo An <anduo@qq.com>  
  
USER root  
  
ARG DEBIAN_FRONTEND=noninteractive  
ADD scripts/ /root/scripts/  
RUN chmod +x /root/scripts/*.sh  
# RUN bash /root/scripts/update-sources-mirror.sh  
# RUN bash /root/scripts/update-conda-mirror.sh  
# libav-tools for matplotlib anim  
# boost for vowpalwabbit  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends libav-tools git && \  
apt-get install -y libboost-program-options-dev zlib1g-dev libboost-python-dev
&& \  
apt-get install -y --no-install-recommends cmake && \  
apt-get install -y apt-utils && \  
apt-get install -y libopencv-dev python-opencv && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER jovyan  
  
  
# Update conda mirrors  
RUN conda install --yes \  
pytorch-cpu torchvision -c pytorch && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
# Add shortcuts to distinguish pip for python2 and python3 envs  
RUN ln -s $CONDA_DIR/envs/python2/bin/pip $CONDA_DIR/bin/pip2 && \  
ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip3  
  
# install vw gbm  
RUN pip install
http://download.pytorch.org/whl/cpu/torch-0.3.1-cp36-cp36m-linux_x86_64.whl  
RUN pip install --upgrade pip  
RUN pip install graphviz vowpalwabbit lightgbm keras tensorflow mxnet \  
xgboost tsfresh Pillow xlearn catboost turicreate scikit-plot \  
scikit-surprise gensim lightfm imbalanced-learn hypertools \  
hyperopt opencv-python fastai progressbar33 tqdm opencv-contrib-python \  
geopandas bokeh  
  
RUN git clone https://github.com/baidu/fast_rgf.git && \  
cd fast_rgf && \  
cd build && \  
cmake .. && \  
make && \  
make install && \  
cd $HOME  
  
RUN echo "completed build."  
  

