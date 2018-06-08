FROM ubuntu:14.04  
MAINTAINER OpenEye <mattg@eyesopen.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get upgrade -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get update && apt-get install -y wget libcairo2-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
  
# Install Conda with Python3  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda3-latest-Linux-x86_64.sh && \  
/opt/conda/bin/conda update --quiet --yes conda && \  
/opt/conda/bin/conda config --system --add channels conda-forge && \  
/opt/conda/bin/conda install --yes pip && \  
/opt/conda/bin/pip install --upgrade pip && \  
conda clean -tipsy  
  
# Install Python/IPython/Jupyter Stack  
RUN conda install --quiet --yes \  
'numpy' \  
'scipy' \  
'pandas' \  
'matplotlib' \  
'seaborn' \  
'scikit-learn' \  
'sympy' \  
'patsy' \  
'statsmodels' \  
'jupyter' \  
'notebook' \  
'ipywidgets' \  
'bokeh' \  
&& conda clean -yt  
  
ENV OE_LICENSE /tmp/oe_license.txt  
  
# Install OE TKs  
COPY requirements.txt /tmp/requirements.txt  
RUN pip --no-cache-dir install -r /tmp/requirements.txt  
  
EXPOSE 8888  
WORKDIR /tmp/notebooks/  
  
CMD jupyter notebook --no-browser --ip=*  

