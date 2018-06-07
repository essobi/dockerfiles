FROM daocloud.io/library/ubuntu:16.04  
MAINTAINER brent <836360140@qq.com>  
  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
COPY sources.list /etc/apt  
  
RUN apt-get update && \  
apt-get install -y wget bzip2 && \  
apt-get clean && \  
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
'tensorflow=1.3.0' \  
&& conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
RUN $CONDA_DIR/bin/pip install \  
'jupyter_kernel_gateway' 'hdfs' && rm -rf ~/.pip ~/.cache  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
# install hadoop 2.7.4  
ENV HADOOP_VERSION 2.7.4  
RUN cd /tmp && wget -q
https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/core/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
&& \  
tar zxf hadoop-${HADOOP_VERSION}.tar.gz && \  
mkdir -p /usr/local/hadoop && \  
mv hadoop-${HADOOP_VERSION}/* /usr/local/hadoop && \  
rm -rf hadoop-${HADOOP_VERSION}*  
  
# set hadoop environment variables  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \  
HADOOP_HOME=/usr/local/hadoop \  
HADOOP_MAPRED_HOME=/usr/local/hadoop \  
HADOOP_COMMON_HOME=/usr/local/hadoop \  
HADOOP_HDFS_HOME=/usr/local/hadoop \  
HADOOP_COMMON_LIB_NATIVE_DIR=/usr/local/hadoop/lib/native \  
HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib" \  
HADOOP_USER_NAME=hdfs \  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${JAVA_HOME}/jre/lib/amd64/server  
  
COPY hdfs-site.xml $HADOOP_HOME/etc/hadoop/  
COPY mapred-site.xml $HADOOP_HOME/etc/hadoop/  
RUN fix-permissions $HADOOP_HOME  
  
RUN mkdir $HOME/workdir  
WORKDIR $HOME/workdir  
EXPOSE 8888  
COPY open_api.ipynb $HOME  
  
ENTRYPOINT ["jupyter", "kernelgateway", "--KernelGatewayApp.ip=0.0.0.0", "--
KernelGatewayApp.api=kernel_gateway.notebook_http", "--
KernelGatewayApp.allow_origin='*'"]  

