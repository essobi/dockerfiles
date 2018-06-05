#  
# Anaconda3-4.3.1  
# kunitaya/anaconda3  
#  
# 2017-06-14  
# CentOS Linux 7.3.1611  
# Python 3.6.0  
# Anaconda3 4.3.1  
FROM kunitaya/centos.jp  
MAINTAINER kunitaya  
  
ENV LANG=ja_JP.UTF-8  
ENV LC_ALL=C  
  
# update yum  
RUN yum makecache fast && \  
yum update -y  
  
# install mariadb (mysql command for development)  
#RUN yum -y install mariadb  
# install Prerequisite package  
RUN yum -y install git bzip2 && \  
git clone https://github.com/yyuu/pyenv.git ~/.pyenv  
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \  
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \  
echo 'eval "$(pyenv init -)"' >> ~/.bashrc  
ENV PYENV_ROOT /root/.pyenv  
ENV PATH $PYENV_ROOT/bin:$PATH  
RUN eval "$(pyenv init -)"  
  
# install Anaconda3  
RUN pyenv install anaconda3-4.3.1 && \  
pyenv rehash && \  
pyenv global anaconda3-4.3.1 && \  
echo 'export PATH="$PYENV_ROOT/versions/anaconda3-4.3.1/bin/:$PATH"' >>
~/.bashrc  
ENV PATH $PYENV_ROOT/versions/anaconda3-4.3.1/bin/:$PATH  
  
# update Conda  
RUN yes | conda update conda  
  
# TODO: CUDA install  
# https://github.com/NVIDIA/nvidia-docker  
# https://github.com/DT42/playground/wiki/Use-CUDA-inside-docker-container  
# https://stackoverflow.com/questions/25185405/using-gpu-from-a-docker-
container  
# Deep Learning Libraries ---  
# install Chainer  
RUN pip install chainer  
  
# install Tensorflow  
RUN pip install tensorflow  
  
# install Keras  
RUN pip install keras  
  
# install Keras-rl  
RUN pip install keras-rl  
  
# TODO: NLR Libraries ---  
# NLTK / Spacy / Vowpal Rabbit / fastText  
# Automated Machine Learning / Ensembling Library  
# install TPOT  
#RUN pip install tpot  
# install heamy  
RUN pip install heamy  
  
# Dimensionality Reduction libraries ---  
# bhtsne (dimensionality reduction)  
RUN cd /usr/local/src && mkdir bhtsne && cd bhtsne && \  
git clone \--depth 1 https://github.com/lvdmaaten/bhtsne.git && \  
g++ sptree.cpp tsne.cpp tsne_main.cpp -o bh_tsne -O2 && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /usr/local/src/*  
  
# Visualization Libraries ---  
# seaborn ggplot plotly altair  
RUN pip install seaborn ggplot plotly altair  
  
# Others Libraries ---  
# install h5py  
RUN conda install h5py  
  
# install simplejson  
RUN pip install simplejson  
  
# install PyMySQL  
RUN pip install PyMySQL  
  
# clear  
RUN yum clean all  
  
CMD ["python"]  

