FROM debian:jessie  
  
MAINTAINER Brent<xuande@inspur.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install wget bzip2 &&\  
apt-get clean all  
  
# install Python + NodeJS with conda  
ENV MINICONDA_VERSION 4.2.12  
ENV CONDA_DIR /opt/conda  
RUN cd /tmp && \  
wget --quiet
https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
&& \  
chmod a+x Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda config --add channels
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ && \  
$CONDA_DIR/bin/conda config --add channels
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ && \  
$CONDA_DIR/bin/conda config --remove channels defaults && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all --quiet --yes && \  
$CONDA_DIR/bin/conda install --yes traitlets requests pip pycurl nodejs
configurable-http-proxy  
ENV PATH=/opt/conda/bin:$PATH  
  
COPY jhub_remote_user_authenticator.tar .  
RUN pip install jupyterhub dockerspawner jhub_remote_user_authenticator.tar
&&\  
rm -rf ~/.cache ~/.npm jhub_remote_user_authenticator.tar  
  
RUN mkdir -p /srv/jupyterhub/ /data  
ADD jupyterhub_config.py /srv/jupyterhub  
WORKDIR /srv/jupyterhub  
  
EXPOSE 8000  
LABEL org.jupyter.service="jupyterhub"  
  
CMD ["jupyterhub"]  

