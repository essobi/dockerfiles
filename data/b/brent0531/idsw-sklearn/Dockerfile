FROM daocloud.io/library/ubuntu:16.04  
MAINTAINER brent <836360140@qq.com>  
  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
COPY sources.list /etc/apt/  
  
RUN apt-get update && \  
apt-get install -y wget bzip2 && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CONDA_DIR=/opt/conda \  
SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100  
ENV PATH=$CONDA_DIR/bin:$PATH \  
HOME=/home/$NB_USER  
  
ADD fix-permissions /usr/local/bin/fix-permissions  
  
RUN chmod a+x /usr/local/bin/fix-permissions  
  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && chown $NB_USER:$NB_GID $CONDA_DIR && \  
fix-permissions $HOME && \  
fix-permissions $CONDA_DIR  
  
USER $NB_USER  
  
ENV MINICONDA_VERSION 4.2.12  
RUN cd /tmp && wget --quiet
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
&& \  
chmod a+x Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
/bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR
&& \  
rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda config --add channels
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ && \  
$CONDA_DIR/bin/conda config --add channels
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ && \  
$CONDA_DIR/bin/conda config --remove channels defaults && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all --quiet --yes && \  
$CONDA_DIR/bin/conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
RUN $CONDA_DIR/bin/conda install --yes \  
'notebook=5.2.*' \  
'pandas=0.21.*' \  
'numpy' \  
'scikit-learn' \  
&& conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN $CONDA_DIR/bin/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \  
'jupyter_kernel_gateway' && rm -rf ~/.pip ~/.cache /home/.cache /home/.pip  
RUN conda install hdfs3 -c
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
COPY idswutils.tar .  
RUN $CONDA_DIR/bin/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \  
idswutils.tar && rm -rf ~/.pip ~/.cache /home/.cache /home/.pip  
  
USER root  
  
RUN mkdir $HOME/workdir  
  
WORKDIR $HOME/workdir  
COPY open_api.ipynb $HOME  
  
EXPOSE 8888  
ENTRYPOINT ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--
KernelGatewayApp.api=kernel_gateway.notebook_http", "--
KernelGatewayApp.allow_origin='*'"]  

