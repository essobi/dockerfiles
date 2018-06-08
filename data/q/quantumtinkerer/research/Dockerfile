FROM jupyter/base-notebook:latest  
  
USER root  
WORKDIR /  
  
# Debian packages  
RUN apt-get update && apt-get install -y --no-install-recommends --fix-missing
\  
autossh \  
bash-completion \  
build-essential \  
cron \  
tree \  
curl \  
dvipng \  
gfortran \  
git \  
tig \  
htop \  
imagemagick \  
inkscape \  
jq \  
keychain \  
latexmk \  
latexdiff \  
less \  
man \  
nano \  
rsync \  
screen \  
tmux \  
biber \  
texlive-bibtex-extra \  
texlive-extra-utils \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-latex-recommended \  
texlive-publishers \  
texlive-science \  
texlive-xetex \  
texlive-lang-cyrillic \  
cm-super \  
vim \  
zsh \  
openssh-server \  
apt-transport-https \  
supervisor \  
gnupg \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add global bash profile  
COPY profile.sh /etc/profile.d/  
  
# Add environment files  
RUN mkdir /environments  
COPY python3.yml dev.yml install_dev.sh /environments/  
  
# Update the root environment  
RUN conda env update -n root -f /environments/python3.yml  
  
# Add a dev environment (e.g. with dev kwant and holoviews)  
# RUN conda env create -p /opt/conda/envs/dev -f /environments/dev.yml  
# Enable `jupyter nbextension`s  
RUN jupyter nbextension enable \--py --sys-prefix ipyparallel && \  
jupyter nbextension enable \--py --sys-prefix jupyter_cms && \  
jupyter nbextension enable \--py --sys-prefix jupyter_dashboards && \  
jupyter nbextension enable \--py --sys-prefix nbserverproxy && \  
jupyter labextension install @jupyter-widgets/jupyterlab-manager \  
@jupyterlab/katex-extension @jupyterlab/latex \  
jupyterlab_bokeh @pyviz/jupyterlab_holoviews  
  
# prevent nb_conda_kernels from overriding our custom kernel manager  
RUN rm /opt/conda/etc/jupyter/jupyter_notebook_config.json  
  
# Add notebook config  
COPY jupyter_notebook_config.py /opt/conda/etc/jupyter  
  
# Register nbdime as a git diff and merge tool  
COPY git* /etc/  
  
# Create parallel profiles and copy the correct config  
RUN ipython profile create --parallel --profile python3 --ipython-dir
/opt/conda/etc/ipython  
# RUN ipython profile create --parallel --profile dev --ipython-dir
/opt/conda/etc/ipython  
COPY ipcluster_config_python3.py
/opt/conda/etc/ipython/profile_python3/ipcluster_config.py  
# COPY ipcluster_config_dev.py
/opt/conda/etc/ipython/profile_dev/ipcluster_config.py  
# setting openblas and mkl variables  
ENV OPENBLAS_NUM_THREADS=1\  
OMP_NUM_THREADS=1\  
MKL_DYNAMIC=FALSE\  
MKL_NUM_THREADS=1\  
CONDA_ALWAYS_COPY=true  
  
# Syncthing installation  
RUN curl -s https://syncthing.net/release-key.txt | apt-key add - && \  
echo "deb https://apt.syncthing.net/ syncthing stable" | tee
/etc/apt/sources.list.d/syncthing.list && \  
apt-get update && apt-get install -y syncthing && apt-get clean  
  
# Install supervisor for automatic starting of syncthing  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
# Fix permissions (required when following the base image)  
RUN fix-permissions /opt/conda  
  
# Cleanup all downloaded conda files  
RUN conda clean --yes --all  
  
# copy startup.sh script and set start-up command  
COPY startup.sh /usr/local/bin  
CMD ["startup.sh"]  
EXPOSE 22  
# Switch back to jovyan to avoid accidental container runs as root  
USER $NB_UID  

