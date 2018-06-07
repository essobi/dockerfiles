# 2018-01-12: This Dockerfile is based on
http://files.fast.ai/setup/paperspace  
# README: https://github.com/MattKleinsmith/dockerfiles/tree/master/fastai  
# 2018-02-01: based on MattKleinsmith's Dockerfile described above  
FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04  
# To allow unicode characters in the terminal  
ENV LANG C.UTF-8  
###########  
## Tools ##  
###########  
RUN apt-get update --fix-missing && apt-get install -y \  
wget \  
vim \  
git \  
unzip  
  
##########  
## Tmux ##  
##########  
RUN apt-get update --fix-missing && apt-get install -y \  
automake \  
autoconf \  
pkg-config \  
build-essential \  
libevent-dev \  
libncurses-dev && \  
git clone https://github.com/tmux/tmux.git && \  
cd tmux && \  
sh autogen.sh && \  
./configure && make && \  
make install  
  
##############  
## Anaconda ##  
##############  
RUN apt-get update --fix-missing && apt-get install -y \  
libglib2.0-0 \  
libsm6 \  
libxext6 \  
libxrender1  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
COPY environment.yml /code/  
  
WORKDIR /code  
  
RUN conda env update  
  
# Solves: `libjpeg.so.8: cannot open shared object file: No such file or
directory`  
# after `from PIL import Image`  
RUN apt-get install -y libjpeg-turbo8  
  
###############  
## Jupyter ##  
###############  
RUN jupyter notebook --generate-config --allow-root && \  
echo "c.NotebookApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_notebook_config.py
&& \  
echo "c.NotebookApp.open_browser = False" >>
~/.jupyter/jupyter_notebook_config.py  
  
RUN /bin/bash -c "\  
source activate fast0tag && \  
conda install -y notebook && \  
conda install -y jupyter_contrib_nbextensions -c conda-forge && \  
jupyter nbextensions_configurator enable --user && \  
jupyter nbextension enable collapsible_headings/main && \  
mkdir -p $(jupyter --data-dir)/nbextensions && \  
cd $(jupyter --data-dir)/nbextensions && \  
git clone https://github.com/lambdalisue/jupyter-vim-binding vim_binding && \  
jupyter nbextension enable vim_binding/vim_binding && \  
pip install jupyterthemes && \  
jt -t onedork -altout -cellw 88% -vim && \  
pip install ipywidgets && \  
jupyter nbextension enable --py widgetsnbextension --sys-prefix"  
  
RUN echo export CUDA_DEVICE_ORDER="PCI_BUS_ID" >> ~/.bashrc  
  
RUN echo 'alias j0="source activate fast0tag && CUDA_VISIBLE_DEVICES=0 jupyter
notebook --port=8880 --allow-root"' >> ~/.bashrc  
  
RUN echo 'alias j1="source activate fast0tag && CUDA_VISIBLE_DEVICES=1 jupyter
notebook --port=8881 --allow-root"' >> ~/.bashrc  
  
RUN echo 'alias j2="source activate fast0tag && CUDA_VISIBLE_DEVICES=2 jupyter
notebook --port=8882 --allow-root"' >> ~/.bashrc  
  
RUN echo 'alias j3="source activate fast0tag && CUDA_VISIBLE_DEVICES=3 jupyter
notebook --port=8883 --allow-root"' >> ~/.bashrc  
  
#############  
## Other ##  
#############  
# https://software.intel.com/en-us/mkl  
RUN /bin/bash -c "\  
source activate fast0tag && \  
conda install mkl-service"  
RUN echo "export MKL_DYNAMIC=FALSE" >> ~/.bashrc  
  
# Convenience  
RUN echo 'source activate fast0tag' >> ~/.bashrc  
RUN echo 'alias tmux-ml="tmux new -s ml -n main -d && \  
tmux new-window -d -n jupyter \"CUDA_VISIBLE_DEVICES=0 jupyter notebook
--port=8880 --allow-root\" && \  
tmux a -t ml"' >> ~/.bashrc  
RUN echo 'tmux-ml' >> ~/.bashrc

