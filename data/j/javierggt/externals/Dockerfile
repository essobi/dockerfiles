FROM javierggt/scipy-notebook  
  
LABEL maintainer="Javier Gonzalez <jgonzalez@icecube.wisc.edu>"  
  
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
fonts-liberation \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
USER $NB_UID  
  
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
rm -rf /home/$NB_USER/.cache/yarn && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
USER root  
  
# Add Tini  
ENV TINI_VERSION v0.18.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
WORKDIR $HOME  
  
# Switch back to NB user to avoid accidental container runs as root  
USER $NB_UID  
  
# Configure container startup  
ENTRYPOINT ["tini", "--"]  
  
CMD ["bash"]  
  
USER root  
  
# add a missing group (same name as the username, same id as the UID)  
RUN addgroup --gid $NB_UID $NB_USER  
  
# OpenCL  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ocl-icd-libopencl1 \  
ocl-icd-opencl-dev \  
clinfo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir -p /etc/OpenCL/vendors && \  
echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd  
  
# additional tools  
RUN apt-get update && apt-get install -y --no-install-recommends \  
subversion \  
nano \  
less \  
rsync \  
openssh-client \  
man-db \  
lsb-release \  
gzip \  
bzip2 \  
xz-utils \  
liblzma5 \  
liblzma-dev \  
zlib1g \  
zlib1g-dev \  
build-essential \  
libsprng2-dev \  
libstarlink-pal-dev \  
htop \  
libgsl-dev \  
libarchive-dev \  
build-essential \  
libgl1-mesa-dev \  
xlibmesa-glu-dev \  
x11-apps \  
mesa-utils \  
libgl1-mesa-glx \  
mc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_UID  
  
# cling, cmake  
RUN conda install --quiet --yes -c QuantStack -c conda-forge \  
'xeus-cling=0.4*' && \  
conda install --quiet --yes \  
'cmake=3.11*' \  
'boost=1.67*' \  
'boost-cpp=1.67*' \  
'cfitsio=3.430*' \  
'urwid=1.3*' \  
'nlopt=2.4*' \  
'suitesparse=4.5*' \  
'zstd=1.3*' && \  
conda clean -tipsy && \  
fix-permissions $CONDA_DIR && \  
fix-permissions /home/$NB_USER  
  
# cdk (build on our own in order to link against conda's ncurses)  
WORKDIR /tmp  
ARG CDK_VERSION=5.0-20160131  
RUN wget --quiet ftp://ftp.invisible-island.net/cdk/cdk-$CDK_VERSION.tgz && \  
echo "c32d075806c231b96ca3778bd24132c7aa0ba9a126f3cebb8a16c59a8b132c22
cdk-$CDK_VERSION.tgz" | sha256sum -c - && \  
tar xzf cdk-$CDK_VERSION.tgz && \  
cd cdk-$CDK_VERSION && \  
./configure --prefix=/opt/conda --with-curses-dir=/opt/conda --enable-rpath
--with-shared && \  
make && \  
make install && \  
cd .. && \  
rm -rf cdk-$CDK_VERSION/ cdk-$CDK_VERSION.tgz && \  
cd /opt/conda/lib && \  
mv libcdk.so.5.0 libcdk.so.6.0.4 && \  
ln -s libcdk.so.6.0.4 libcdk.so.6.0 && \  
ln -s libcdk.so.6.0 libcdk.so.6 && \  
ln -s libcdk.so.6 libcdk.so  
  
WORKDIR /home/$NB_USER

