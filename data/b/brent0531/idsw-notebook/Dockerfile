# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM ubuntu:16.04  
MAINTAINER Brent <836360140@qq.com>  
  
USER root  
# Install all OS dependencies for notebook server that starts but lacks all  
# features (e.g., download as all possible file formats)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
bzip2 \  
sudo \  
locales \  
fonts-liberation \  
build-essential \  
openjdk-8-jdk \  
git \  
libkrb5-dev \  
vim \  
unzip \  
supervisor \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Tini  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.10.0/tini && \  
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Configure environment  
ENV CONDA_DIR=/opt/conda \  
SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100 \  
HOME=/home/$NB_USER \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
  
ADD fix-permissions /usr/local/bin/fix-permissions  
RUN chmod a+x /usr/local/bin/fix-permissions  
# Create brent user with UID=1000 and in the 'users' group  
# and make sure these dirs are writable by the `users` group.  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER:$NB_GID $CONDA_DIR && \  
fix-permissions $HOME && \  
fix-permissions $CONDA_DIR  
  
USER $NB_USER  
RUN mkdir /home/$NB_USER/work && \  
fix-permissions /home/$NB_USER  
  
# Install conda as brent and check the md5 sum provided on the download site  
ENV MINICONDA_VERSION 4.2.12  
ENV PATH=$CONDA_DIR/bin:$PATH  
RUN cd /tmp && \  
wget --quiet
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
&& \  
/bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR
&& \  
rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all --quiet --yes && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
# install notebook jupyterhub  
RUN $CONDA_DIR/bin/conda install --quiet --yes \  
'notebook=5.2.*' \  
'jupyterhub=0.8.*' \  
'pandas=0.21.*' \  
'hdijupyterutils' \  
'autovizwidget' \  
'nose' \  
'mock' \  
'numpy' \  
'requests' \  
'scikit-learn' \  
'matplotlib' \  
'tensorflow=1.3.0' \  
&& conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
# install sparkmagic  
COPY sparkmagic.tar /tmp/  
RUN pip install /tmp/sparkmagic.tar && \  
fix-permissions $CONDA_DIR  
RUN $CONDA_DIR/bin/jupyter-kernelspec install --user
$CONDA_DIR/lib/python3.5/site-packages/sparkmagic/kernels/pysparkkernel  
  
# install jieba nltk  
RUN pip install jieba nltk jupyter_kernel_gateway && \  
rm -rf ~/.pip ~/.cache  
  
RUN conda install hdfs3 -c conda-forge && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN pip install notebook==5.3.0 && \  
fix-permissions $CONDA_DIR && \  
rm -rf ~/.pip ~/.cache  
  
COPY hdfscontents-jupyter.tar /tmp  
RUN pip install /tmp/hdfscontents-jupyter.tar && \  
fix-permissions $CONDA_DIR && \  
rm -rf ~/.pip ~/.cache  
  
COPY idswutils.tar /tmp  
RUN pip install /tmp/idswutils.tar && \  
fix-permissions $CONDA_DIR && \  
rm -rf ~/.pip ~/.cache  
  
USER root  
# set sparkmagic configuation path  
ENV SPARKMAGIC_CONF_DIR="/etc/jupyter" \  
SPARKMAGIC_CONF_FILE="sparkmagic.json" \  
JUPYTER_CONFIG_DIR="/etc/jupyter"  
RUN fix-permissions /home/$NB_USER/  
  
WORKDIR $HOME  
  
# hide jupyter logo.  
RUN mkdir -p /etc/jupyter/custom && echo '#header-container {display: none
!important;}' > /etc/jupyter/custom/custom.css  
  
COPY start.sh /usr/local/bin/  
COPY start-notebook.sh /usr/local/bin/  
COPY start-singleuser.sh /usr/local/bin/  
COPY jupyter_notebook_config.py /etc/jupyter/  
COPY sparkmagic.json /etc/jupyter/  
RUN fix-permissions /etc/jupyter/ && \  
fix-permissions $CONDA_DIR && \  
chmod +x /usr/local/bin/start-* && \  
jupyter nbextension enable \--py widgetsnbextension && \  
chmod 777 -R /etc/jupyter && \  
rm -rf ~/.pip ~/.cache /tmp/*.tar /tmp/*.gz /home/.cache /home/.pip  
  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 8888  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["/usr/bin/supervisord"]  
  
# switch user  
USER $NB_USER  

