FROM nvidia/cuda:8.0-cudnn6-runtime-ubuntu16.04  
# Starting from tensorflow  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
rsync \  
software-properties-common \  
unzip \  
wget \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
# Download needed scripts from base-notebook repo  
ADD https://raw.githubusercontent.com/jupyter/docker-stacks/master/base-
notebook/fix-permissions \  
/usr/local/bin/fix-permissions  
RUN chmod 4755 /usr/local/bin/fix-permissions  
  
# Starting from base-notebook  
# Install all OS dependencies for notebook server that starts but lacks all  
# features (e.g., download as all possible file formats)  
ENV DEBIAN_FRONTEND noninteractive  
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
ENV CONDA_DIR=/opt/conda \  
SHELL=/bin/bash \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
ENV PATH=$CONDA_DIR/bin:$PATH \  
HOME=/home/$NB_USER  
  
# Create jovyan user with UID=1000 and in the 'users' group  
# and make sure these dirs are writable by the `users` group.  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
adduser $NB_USER sudo && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER:$NB_GID $CONDA_DIR && \  
fix-permissions $HOME && \  
fix-permissions $CONDA_DIR  
  
# Setup work directory for backward-compatibility  
RUN mkdir /home/$NB_USER/work && \  
fix-permissions /home/$NB_USER  
  
USER $NB_USER  
  
# Install conda as jovyan and check the md5 sum provided on the download site  
ENV MINICONDA_VERSION 4.3.30  
RUN cd /tmp && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
&& \  
echo "0b80a152332a4ce5250f3c09589c7a81
*Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh" | md5sum -c - && \  
/bin/bash Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh -f -b -p $CONDA_DIR
&& \  
rm Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all --quiet --yes && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
# Install Jupyter Notebook and Hub  
RUN conda install --quiet --yes \  
'notebook=5.2.*' \  
'jupyterhub=0.8.*' \  
'jupyterlab=0.28.*' \  
&& conda clean -tipsy \  
&& fix-permissions $CONDA_DIR  
  
EXPOSE 8888  
WORKDIR $HOME  
  
# Add local files as late as possible to avoid cache busting  
USER root  
ADD https://raw.githubusercontent.com/jupyter/docker-stacks/master/base-
notebook/start.sh /usr/local/bin/  
ADD https://raw.githubusercontent.com/jupyter/docker-stacks/master/base-
notebook/start-notebook.sh /usr/local/bin/  
ADD https://raw.githubusercontent.com/jupyter/docker-stacks/master/base-
notebook/start-singleuser.sh /usr/local/bin/  
ADD https://raw.githubusercontent.com/jupyter/docker-stacks/master/base-
notebook/jupyter_notebook_config.py /etc/jupyter/  
RUN chmod 4755 /usr/local/bin/start-notebook.sh /usr/local/bin/start-
singleuser.sh /usr/local/bin/start.sh  
RUN fix-permissions /etc/jupyter/  
  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Starting from minimal-notebook  
# Install all OS dependencies for fully functional notebook server  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
build-essential \  
emacs \  
git \  
inkscape \  
jed \  
libsm6 \  
libxext-dev \  
libxrender1 \  
lmodern \  
pandoc \  
python-dev \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-xetex \  
vim \  
unzip \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Starting from scipy-notebook  
USER root  
  
# libav-tools for matplotlib anim  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libav-tools && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
# Install Python 3 packages  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
RUN conda install --quiet --yes \  
'nomkl' \  
'ipywidgets=7.0*' \  
'pandas=0.19*' \  
'numexpr=2.6*' \  
'matplotlib=2.0*' \  
'scipy=0.19*' \  
'seaborn=0.7*' \  
'scikit-learn=0.18*' \  
'scikit-image=0.12*' \  
'sympy=1.0*' \  
'cython=0.25*' \  
'patsy=0.4*' \  
'statsmodels=0.8*' \  
'cloudpickle=0.2*' \  
'dill=0.2*' \  
'numba=0.31*' \  
'bokeh=0.12*' \  
'sqlalchemy=1.1*' \  
'hdf5=1.8.17' \  
'h5py=2.6*' \  
'vincent=0.4.*' \  
'beautifulsoup4=4.5.*' \  
'protobuf=3.*' \  
'xlrd' && \  
conda clean -tipsy && \  
jupyter nbextension enable \--py widgetsnbextension --sys-prefix && \  
fix-permissions $CONDA_DIR  
  
# Install facets which does not have a pip or conda package at the moment  
RUN cd /tmp && \  
git clone https://github.com/PAIR-code/facets.git && \  
cd facets && \  
jupyter nbextension install facets-dist/ --sys-prefix && \  
rm -rf facets && \  
fix-permissions $CONDA_DIR  
  
# Import matplotlib the first time to build the font cache.  
ENV XDG_CACHE_HOME /home/$NB_USER/.cache/  
RUN MPLBACKEND=Agg python -c "import matplotlib.pyplot"  
  
USER root  
RUN fix-permissions /home/$NB_USER  
USER $NB_USER  
  
# Starting custom tensorflow  
# Change user to install things in the Conda env  
RUN ["bash", "-c", "source activate root"]  
  
# Install Tensorflow GPU version  
RUN pip install tensorflow-gpu  
  
# Install keras  
RUN pip install "keras>=2.0"  

