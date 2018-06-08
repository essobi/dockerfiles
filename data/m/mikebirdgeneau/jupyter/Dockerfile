FROM python:latest  
  
USER root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -yq --no-install-recommends \  
wget \  
bzip2 \  
ca-certificates \  
sudo \  
locales \  
git \  
vim \  
jed \  
emacs \  
build-essential \  
python-dev \  
unzip \  
libsm6 \  
pandoc \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
libxrender1 \  
fonts-dejavu \  
gfortran \  
gcc \  
libnetcdf-dev \  
libhdf5-dev \  
libproj-dev \  
libgeos++-dev \  
libgeos-dev \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
# Install Tini  
RUN wget --quiet https://github.com/krallin/tini/releases/download/v0.9.0/tini
&& \  
echo "faafbfb5b079303691a939a747d7f60591f2143164093727e870b289a44d9872 *tini"
| sha256sum -c - && \  
mv tini /usr/local/bin/tini && \  
chmod +x /usr/local/bin/tini  
  
# Configure environment  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
ENV SHELL /bin/bash  
ENV NB_USER jupyter  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Create user with UID=1000 and in the 'users' group  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER $CONDA_DIR  
  
USER $NB_USER  
  
# Setup home directory  
RUN mkdir /home/$NB_USER/work && \  
mkdir /home/$NB_USER/.jupyter && \  
mkdir -p -m 700 /home/$NB_USER/.local/share/jupyter && \  
echo "cacert=/etc/ssl/certs/ca-certificates.crt" > /home/$NB_USER/.curlrc  
  
# Install conda as NB_USER  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-3.19.0-Linux-x86_64.sh && \  
echo "9ea57c0fdf481acf89d816184f969b04bc44dea27b258c4e86b1e3a25ff26aa0
*Miniconda3-3.19.0-Linux-x86_64.sh" | sha256sum -c - && \  
/bin/bash Miniconda3-3.19.0-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda3-3.19.0-Linux-x86_64.sh && \  
$CONDA_DIR/bin/conda install --quiet --yes conda==3.19.1 && \  
$CONDA_DIR/bin/conda config --system --add channels conda-forge && \  
conda clean -tipsy  
  
# R packages  
RUN conda config --add channels r && \  
conda install --quiet --yes \  
'r-base=3.3*' \  
'r-irkernel=0.6*' \  
'r-plyr=1.8*' \  
'r-devtools=1.11*' \  
'r-dplyr=0.4*' \  
'r-ggplot2=2.1*' \  
'r-tidyr=0.5*' \  
'r-shiny=0.13*' \  
'r-rmarkdown=0.9*' \  
'r-forecast=7.1*' \  
'r-stringr=1.0*' \  
'r-rsqlite=1.0*' \  
'r-reshape2=1.4*' \  
'r-nycflights13=0.2*' \  
'r-caret=6.0*' \  
'r-rcurl=1.95*' \  
'r-randomforest=4.6*' && conda clean -tipsy  
  
# Temporary workaround for https://github.com/jupyter/docker-stacks/issues/210  
# Stick with jpeg 8 to avoid problems with R packages  
RUN echo "jpeg 8*" >> /opt/conda/conda-meta/pinned  
  
# Install JupyterHub to get the jupyterhub-singleuser startup script  
RUN pip --no-cache-dir install 'jupyterhub==0.5'  
  
# Install Python 3 packages  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
RUN conda install --quiet --yes \  
'pandas=0.18*' \  
'numexpr=2.5*' \  
'matplotlib=1.5*' \  
'scipy=0.17*' \  
'seaborn=0.7*' \  
'scikit-learn=0.17*' \  
'scikit-image=0.11*' \  
'sympy=1.0*' \  
'cython=0.23*' \  
'patsy=0.4*' \  
'statsmodels=0.6*' \  
'cloudpickle=0.1*' \  
'dill=0.2*' \  
'numba=0.23*' \  
'bokeh=0.11*' \  
'h5py=2.5*' && \  
conda install -c conda-forge ipywidgets && \  
conda remove --quiet --yes --force qt pyqt && \  
conda clean -tipsy  
# Activate ipywidgets extension in the environment that runs the notebook
server  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
# Install Python 2 packages  
# Remove pyqt and qt pulled in for matplotlib since we're only ever going to  
# use notebook-friendly backends in these images  
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 \  
'ipython=4.2*' \  
'pandas=0.18*' \  
'numexpr=2.5*' \  
'matplotlib=1.5*' \  
'scipy=0.17*' \  
'seaborn=0.7*' \  
'scikit-learn=0.17*' \  
'scikit-image=0.11*' \  
'sympy=1.0*' \  
'cython=0.23*' \  
'patsy=0.4*' \  
'statsmodels=0.6*' \  
'cloudpickle=0.1*' \  
'dill=0.2*' \  
'numba=0.23*' \  
'bokeh=0.11*' \  
'h5py=2.5*' \  
'pyzmq' && \  
conda install -c conda-forge -p $CONDA_DIR/envs/python2 python=2.7 ipywidgets
&& \  
conda remove -n python2 --quiet --yes --force qt pyqt && \  
conda clean -tipsy  
  
# Add shortcuts to distinguish pip for python2 and python3 envs  
RUN ln -s $CONDA_DIR/envs/python2/bin/pip $CONDA_DIR/bin/pip2 && \  
ln -s $CONDA_DIR/bin/pip $CONDA_DIR/bin/pip3  
  
# Configure ipython kernel to use matplotlib inline backend by default  
RUN mkdir -p $HOME/.ipython/profile_default/startup  
COPY mplimporthook.py $HOME/.ipython/profile_default/startup/  
  
# Install Jupyter notebook as NB_USER  
RUN conda install --quiet --yes \  
'notebook=4.2*' \  
&& conda clean -tipsy  
  
# Install JupyterHub to get the jupyterhub-singleuser startup script  
RUN pip --no-cache-dir install 'jupyterhub==0.5'  
  
USER root  
  
# Install Python 2 kernel spec globally to avoid permission problems when
NB_UID  
# switching at runtime.  
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install  
  
# Configure container startup as root  
EXPOSE 8888  
WORKDIR /home/$NB_USER/work  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Add local files as late as possible to avoid cache busting  
COPY start-notebook.sh /usr/local/bin/  
COPY start-singleuser.sh /usr/local/bin/  
COPY jupyter_notebook_config.py /home/$NB_USER/.jupyter/  
RUN chown -R $NB_USER:users /home/$NB_USER/.jupyter  
  
# Add any extra requirements. Done at end to avoid cache busting.  
ADD requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
RUN wget https://github.com/matplotlib/basemap/archive/v1.0.7rel.tar.gz; pip
install v1.0.7rel.tar.gz; rm v1.0.7rel.tar.gz  
  
ADD install_packages.R install_packages.R  
RUN /usr/bin/Rscript install_packages.R; rm install_packages.R  
  
EXPOSE 8888  
USER $NB_USER  

