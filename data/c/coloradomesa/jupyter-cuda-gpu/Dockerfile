FROM nvidia/cuda:9.0-cudnn7-devel  
  
USER root  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
wget \  
curl \  
bzip2 \  
ca-certificates \  
sudo \  
locales \  
fonts-liberation \  
python3 \  
python3-pip \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
#install bazel for later  
RUN apt-get update && apt-get install openjdk-8-jdk -y && \  
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8"
| sudo tee /etc/apt/sources.list.d/bazel.list && \  
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add - && \  
apt-get update && apt-get install bazel -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
build-essential \  
emacs \  
inkscape \  
jed \  
libsm6 \  
libxext-dev \  
libxrender1 \  
lmodern \  
netcat \  
pandoc \  
python-dev \  
unzip \  
vim \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CONDA_DIR=/opt/conda \  
SHELL=/bin/bash \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
NB_USER=jovyan \  
NB_UID=1000 \  
NB_GID=100  
ENV PATH=$CONDA_DIR/bin:$PATH  
  
ADD fix-permissions /usr/local/bin/fix-permissions  
RUN chmod +x /usr/local/bin/fix-permissions  
  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER:$NB_GID $CONDA_DIR && \  
chmod g+w /etc/passwd /etc/group && \  
echo "$NB_USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
fix-permissions $HOME && \  
fix-permissions $CONDA_DIR  
  
USER $NB_UID  
  
#test that sudo works  
RUN sudo cat /etc/sudoers  
  
RUN mkdir /home/$NB_USER/work && \  
fix-permissions /home/$NB_USER  
  
ENV MINICONDA_VERSION=4.3.30  
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
rm -rf /home/$NB_USER/.cache/yarn && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
RUN conda install --quiet --yes \  
-c aaronzs \  
'notebook=5.4.*' \  
'jupyterhub=0.8.*' \  
'jupyterlab=0.31.*' \  
'tornado=4.*' \  
&& conda clean -tipsy && \  
jupyter labextension install @jupyterlab/hub-extension@^0.8.0 && \  
npm cache clean && \  
rm -rf $CONDA_DIR/share/jupyter/lab/staging && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
RUN conda install --quiet --yes \  
-c aaronzs \  
'nomkl' \  
'ipywidgets' \  
'pandas' \  
'numexpr' \  
'matplotlib' \  
'scipy' \  
'seaborn' \  
'scikit-learn' \  
'scikit-image' \  
'sympy' \  
'cython' \  
'patsy' \  
'statsmodels' \  
'cloudpickle' \  
'dill' \  
'numba' \  
'bokeh' \  
'sqlalchemy' \  
'hdf5' \  
'h5py' \  
'vincent' \  
'beautifulsoup4' \  
'protobuf' \  
'xlrd' \  
'keras' && \  
conda remove --quiet --yes --force qt pyqt && \  
conda clean -tipsy && \  
# Activate ipywidgets extension in the environment that runs the notebook
server  
jupyter nbextension enable --py widgetsnbextension --sys-prefix && \  
# Also activate ipywidgets extension for JupyterLab  
jupyter labextension install @jupyter-widgets/jupyterlab-manager@^0.33.1 && \  
jupyter labextension install jupyterlab_bokeh@^0.4.0 && \  
npm cache clean && \  
rm -rf $CONDA_DIR/share/jupyter/lab/staging && \  
rm -rf /home/$NB_USER/.cache/yarn && \  
rm -rf /home/$NB_USER/.node-gyp  
RUN python3 -m pip install jupyter_contrib_nbextensions  
RUN python3 -m pip install git+https://github.com/data-8/nbgitpuller \  
plotly  
# jupyterlab extensions  
RUN jupyter labextension install @jupyterlab/hub-extension && \  
jupyter labextension install @jupyter-widgets/jupyterlab-manager  
# activation  
RUN jupyter lab build  
  
# install or activate other kernels  
RUN conda create --quiet --yes -n ipykernel_py2 python=2 ipykernel && \  
python -m ipykernel install --user  
RUN conda config --add channels conda-forge && \  
conda create --quiet --yes -n java_env scijava-jupyter-kernel  
RUN bash -c "source activate java_env" && \  
bash -c "source activate ipykernel_py2"  
  
# specific numpy version for tensorflow  
RUN python3 -m pip install numpy==1.14  
  
#build tensorflow 1.5 from sources  
#RUN git clone https://github.com/tensorflow/tensorflow && \  
# cd tensorflow && \  
# git checkout r1.5 && \  
RUN jupyter kernelspec list  
  

