FROM drunkar/cuda-caffe-anaconda-chainer  
MAINTAINER drunkar <drunkars.p@gmail.com>  
  
##############################################################################  
# MeCab  
##############################################################################  
RUN sudo apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 git make curl
xz-utils  
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git &&
cd mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -n -y  
RUN sudo /opt/conda/bin/pip install mecab-python3  
  

