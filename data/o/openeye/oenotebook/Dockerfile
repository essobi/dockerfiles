FROM ubuntu:14.04  
MAINTAINER OpenEye <mattg@eyesopen.com>  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-get update && apt-get install -y wget libcairo2-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
  
# Install Conda  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda-latest-
Linux-x86_64.sh && \  
bash Miniconda-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda-latest-Linux-x86_64.sh && \  
/opt/conda/bin/conda update --quiet --yes conda && \  
/opt/conda/bin/pip install --upgrade pip  
  
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
'ipywidgets' \  
'bokeh' \  
&& conda clean -yt  
  
# Install OE TKs  
COPY requirements.txt /tmp/requirements.txt  
RUN pip --no-cache-dir install -r /tmp/requirements.txt && \  
pip --no-cache-dir install --pre --extra-index-url
https://pypi.anaconda.org/OpenEye/channel/beta/simple OpenEye-oenotebook  
EXPOSE 8888  
ENV OE_LICENSE /tmp/oe_license.txt  
  
WORKDIR /tmp/notebooks/  
  
CMD jupyter notebook --no-browser --ip=*  

