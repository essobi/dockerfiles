FROM ubuntu:16.04  
  
##########################################################################################################  
# Copied with some changes https://github.com/jupyter/docker-
stacks/blob/master/base-notebook/Dockerfile #  
##########################################################################################################  
  
USER root  
  
# Install all OS dependencies for notebook server that starts but lacks all  
# features (e.g., download as all possible file formats)  
RUN apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
wget \  
bzip2 \  
ca-certificates \  
sudo \  
locales \  
fonts-liberation \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
# Install Tini  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.10.0/tini && \  
echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:/cling/bin:$PATH  
ENV SHELL /bin/bash  
ENV NB_USER jovyan  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
  
# Create jovyan user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER $CONDA_DIR  
  
USER $NB_USER  
  
# Setup work directory for backward-compatibility  
RUN mkdir /home/$NB_USER/work  
  
# Install conda as jovyan and check the md5 sum provided on the download site  
ENV MINICONDA_VERSION 4.3.21  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
&& \  
echo "c1c15d3baba15bf50293ae963abef853
*Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \  
/bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR
&& \  
rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all && \  
conda clean -tipsy  
  
# Install Jupyter Notebook and Hub  
RUN conda install --quiet --yes \  
'notebook=5.0.*' \  
'jupyterhub=0.7.*' \  
'jupyterlab=0.24.*' \  
&& conda clean -tipsy  
  
USER root  
  
EXPOSE 8888  
WORKDIR $HOME  
  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
##########################################################################################################  
##########################################################################################################  
##########################################################################################################  
  
# Install cling dependencies  
USER root  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends git g++ debhelper devscripts gnupg  
  
# Create cling folder  
RUN mkdir /cling  
RUN chown -R $NB_USER:users /cling  
WORKDIR /cling  
  
# Add local files as late as possible to avoid cache busting  
COPY start.sh /usr/local/bin/  
COPY start-notebook.sh /usr/local/bin/  
COPY start-singleuser.sh /usr/local/bin/  
COPY jupyter_notebook_config.py /etc/jupyter/  
RUN chown -R $NB_USER:users /etc/jupyter/  
RUN chmod +x /usr/local/bin/start.sh /usr/local/bin/start-notebook.sh
/usr/local/bin/start-singleuser.sh  
  
# Download cling from https://root.cern.ch/download/cling/  
USER $NB_USER  
COPY download_cling.py download_cling.py  
RUN python download_cling.py  
  
# install cling kernel  
WORKDIR /cling/share/cling/Jupyter/kernel  
RUN pip install -e .  
RUN jupyter-kernelspec install --user cling-cpp11  
  
WORKDIR $HOME  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_USER  

