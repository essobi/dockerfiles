FROM debian:latest  
MAINTAINER David Gasquez <davidgasquez@gmail.com>  
  
# Update and install system packages  
RUN apt-get update -y && \  
apt-get install --no-install-recommends --allow-unauthenticated -y -q \  
curl build-essential wget bzip2 sudo ca-certificates && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Declare environment variables  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV NB_USER local  
ENV NB_UID 1000  
# Create local user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER $CONDA_DIR  
  
RUN mkdir /work && chown $NB_USER /work  
  
# Switch to local user  
USER $NB_USER  
  
# Setup local home directory  
RUN mkdir /home/$NB_USER/work && \  
mkdir /home/$NB_USER/.jupyter  
  
# Install and update Miniconda  
RUN wget --quiet http://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -f -b -p $CONDA_DIR && \  
rm ~/miniconda.sh  
  
# Install Anaconda  
RUN conda install --quiet --yes conda conda-env && \  
conda clean -tipsy  
  
# Copy requirements file  
COPY requirements.yml /tmp/requirements.yml  
  
# Install requirements into current environment .  
RUN conda env update -f /tmp/requirements.yml && \  
rm -rf /home/$NB_USER/.cache/pip/*  
  
# Enable Jupyter Notebook extensions  
RUN jupyter serverextension enable \--py jupyterlab --sys-prefix  
  
# Add custom configuration  
COPY config/jupyter_notebook_config.py /home/$NB_USER/.jupyter/  
  
# Create folder  
WORKDIR "/work"  
  
# Start Notebook  
CMD jupyter lab  

