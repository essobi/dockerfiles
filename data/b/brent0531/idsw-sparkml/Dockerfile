FROM ubuntu:16.04  
MAINTAINER brent <836360140@qq.com>  
  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
COPY sources.list /etc/apt  
  
RUN apt-get update && \  
apt-get install -y wget bzip2 openjdk-8-jdk && \  
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
$CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all --quiet --yes && \  
conda clean -tipsy && \  
rm -rf /home/$NB_USER/.cache/yarn && \  
fix-permissions $CONDA_DIR  
  
RUN $CONDA_DIR/bin/conda install --yes \  
'notebook=5.2.*' \  
'pandas=0.21.*' \  
'numpy' \  
&& conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN $CONDA_DIR/bin/pip install \  
'jupyter_kernel_gateway' 'findspark' && \  
fix-permissions $CONDA_DIR && rm -rf ~/.pip ~/.cache  
  
USER root  
  
RUN wget --quiet
https://archive.apache.org/dist/spark/spark-2.1.0/spark-2.1.0-bin-
hadoop2.7.tgz && \  
tar xvf spark-2.1.0-bin-hadoop2.7.tgz && \  
mv spark-2.1.0-bin-hadoop2.7 spark && \  
mv spark /usr/local/ && \  
rm -rf spark-2.1.0-bin-hadoop2.7.tgz  
  
ENV SPARK_HOME=/usr/local/spark  
ENV PATH=$SPARK_HOME/bin:$PATH  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
USER root  
EXPOSE 8888  
RUN mkdir $HOME/workdir  
WORKDIR $HOME/workdir  
  
COPY open_api.ipynb $HOME  
  
ENTRYPOINT ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--
KernelGatewayApp.api=kernel_gateway.notebook_http", "--
KernelGatewayApp.allow_origin='*'"]  

