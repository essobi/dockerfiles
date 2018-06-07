# Copyright (c) Because  
# Distributed under the terms of the Modified BSD License.  
# Ubuntu 16.04 (xenial) from 2017-07-23  
# https://github.com/docker-library/official-
images/commit/0ea9b38b835ffb656c497783321632ec7f87b60c  
FROM
ubuntu@sha256:84c334414e2bfdcae99509a6add166bbb4fa4041dc3fa6af08046a66fed3005f  
LABEL maintainer="Marius <marius@marius.ninja>"  
USER root  
  
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
fonts-liberation  
  
# add rclone (with fuse for mounts, and ssh for Python paramiko)  
RUN apt-get install -yq --no-install-recommends \  
fuse \  
libfuse2 \  
unzip \  
openssh-client \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD http://downloads.rclone.org/rclone-current-linux-amd64.zip /tmp/  
RUN cd /tmp && \  
unzip rclone-current-linux-amd64.zip && \  
cd rclone-*-linux-amd64 && \  
cp rclone /usr/sbin && \  
chown root:root /usr/sbin/rclone && \  
chmod 755 /usr/sbin/rclone  
  
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
NB_USER=jupy \  
NB_UID=1000 \  
NB_GID=100 \  
LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
ENV PATH=$CONDA_DIR/bin:$PATH \  
HOME=/home/$NB_USER  
  
ADD fix-permissions /usr/local/bin/fix-permissions  
  
# Create jupy user with UID=1000 and in the 'users' group  
# and make sure these dirs are writable by the `users` group.  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown $NB_USER:$NB_GID $CONDA_DIR && \  
fix-permissions $HOME && \  
fix-permissions $CONDA_DIR  
  
# Setup work directory for backward-compatibility  
RUN mkdir /home/$NB_USER/work && \  
fix-permissions /home/$NB_USER  
  
# Install conda as jupy and check the md5 sum provided on the download site  
ENV MINICONDA_VERSION 4.3.27  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-${MINICONDA_VERSION}-Linux-x86_64.sh
-O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -u -b -p /opt/conda && \  
$CONDA_DIR/bin/conda config --system --prepend channels conda-forge && \  
$CONDA_DIR/bin/conda config --system --set auto_update_conda false && \  
$CONDA_DIR/bin/conda config --system --set show_channel_urls true && \  
$CONDA_DIR/bin/conda update --all --quiet --yes && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR  
  
# Install Jupyter Notebook and Hub  
# RUN conda install --quiet --yes jupyterhub -c conda-forge  
# RUN conda install --quiet --yes jupyterlab -c conda-forge  
RUN conda install --quiet --yes jupyter_dashboards -c conda-forge  
RUN conda install --quiet --yes pandas -c conda-forge  
RUN conda install --quiet --yes matplotlib -c conda-forge  
RUN conda install --quiet --yes plotly -c conda-forge  
RUN conda install --quiet --yes paramiko -c conda-forge  
RUN conda install --quiet --yes scikit-learn -c conda-forge  
RUN conda clean -tipsy  
  
# Add local files as late as possible to avoid cache busting  
COPY start.sh /usr/local/bin/  
COPY start-notebook.sh /usr/local/bin/  
COPY start-singleuser.sh /usr/local/bin/  
COPY jupyter_notebook_config.py /etc/jupyter/  
RUN fix-permissions /etc/jupyter/  
  
EXPOSE 8888  
USER $NB_USER  
WORKDIR $HOME  
  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Switch back to jupy to avoid accidental container runs as root  
USER $NB_USER  

