FROM ubuntu:14.04  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget
libcairo2-dev  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
ENV OE_LICENSE /tmp/oe_license.txt  
  
# Install Conda with Python3  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda3-latest-Linux-x86_64.sh && \  
/opt/conda/bin/conda update --quiet --yes conda && \  
/opt/conda/bin/conda install --yes pip && \  
/opt/conda/bin/pip install --upgrade pip==8.1.1  
  
# Install OE TKs  
COPY requirements.txt /tmp/requirements.txt  
RUN pip --no-cache-dir install -r /tmp/requirements.txt  

