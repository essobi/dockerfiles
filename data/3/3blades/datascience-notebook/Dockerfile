FROM 3blades/core-server:build-119 AS core  
FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
MAINTAINER 3Blades <contact@3blades.io>  
  
# Install Python3.6, link python3 to 3.6  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
software-properties-common \  
&& add-apt-repository -y ppa:jonathonf/python-3.6 \  
&& apt update -y \  
&& apt --assume-yes install -y \  
python3.6 \  
&& unlink /usr/bin/python3 \  
&& ln -s /usr/bin/python3.6 /usr/bin/python3  
  
# Install all OS dependencies for notebook server that starts but lacks all  
# features (e.g., download as all possible file formats)  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
apt-transport-https \  
build-essential \  
bzip2 \  
ca-certificates \  
cmake \  
emacs \  
fonts-liberation \  
gcc \  
gfortran \  
git \  
graphviz \  
fonts-dejavu \  
inkscape \  
jed \  
libav-tools \  
libavcodec-dev \  
libavformat-dev \  
libblas-dev \  
libdc1394-22-dev \  
libffi-dev \  
libgtk2.0-dev \  
libjpeg-dev \  
liblapack-dev \  
libgtk2.0-dev \  
libjasper-dev \  
libpng-dev \  
libpq-dev \  
libmysqlclient-dev \  
libopencv-dev \  
libpython3.6-dev \  
libssl-dev \  
libtiff-dev \  
libsm6 \  
libswscale-dev \  
libtbb2 \  
libxft-dev \  
libxrender1 \  
locales \  
openmpi-bin \  
pandoc \  
pkg-config \  
python-dev \  
python-pip \  
python-setuptools \  
python3-pip \  
python3-setuptools \  
sudo \  
texlive-latex-base \  
texlive-latex-extra \  
texlive-fonts-extra \  
texlive-fonts-recommended \  
texlive-generic-recommended \  
texlive-xetex \  
unzip \  
vim \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'en_US.UTF-8' > /etc/locale.gen && \  
locale-gen  
  
# Install Tini  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.10.0/tini \  
&& echo "1361527f39190a7338a0b434bd8c88ff7233ce7b9a4876f3315c22fce7eca1b0
*tini" | sha256sum -c - \  
&& mv tini /usr/local/bin/tini \  
&& chmod +x /usr/local/bin/tini  
  
# Install virtualenv  
RUN pip install virtualenv \  
&& pip3 install virtualenv  
  
# Upgrade pip and pip3  
RUN pip install --upgrade pip  
RUN pip3 install --upgrade pip  
  
# Install setuptools  
RUN pip install --upgrade pip setuptools  
  
# Install pytests for notebook tests  
RUN pip install pytest  
  
# Install Jupyter Notebook  
RUN pip install --no-cache-dir \  
jupyter \  
jupyterlab  
  
# Set up kernel for Python2  
RUN python2 -m pip install ipykernel  
RUN python2 -m ipykernel install --user  
  
# Install Python2 packages  
RUN pip2 install --user \  
graphviz \  
h5py \  
matplotlib \  
nose \  
numpy \  
pandas \  
Pillow \  
pyyaml \  
scipy \  
scikit-learn \  
sympy  
  
# Install Python3 packages  
RUN pip3 install --user \  
graphviz \  
h5py \  
matplotlib \  
nose \  
numpy \  
pandas \  
Pillow \  
pyyaml \  
scipy \  
scikit-learn \  
sympy  
  
# Install Keras and TensorFlow w/ Python2  
RUN pip2 install tensorflow-gpu  
RUN pip2 install keras  
  
# Install Keras and TensorFlow w/ Python3  
RUN pip3 install tensorflow-gpu  
RUN pip3 install keras  
  
# Configure container startup as root  
EXPOSE 8080  
WORKDIR /home/work  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  
  
# Configure ipython kernel to use matplotlib inline backend by default  
RUN mkdir -p /root/.ipython/profile_default/startup  
  
# Add local files as late as possible to avoid cache busting  
COPY mplimporthook.py /root/.ipython/profile_default/startup/  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
COPY \--from=core runner /runner  
COPY start-notebook.sh /usr/local/bin/  
  
# Add some notebook tests, tests can be run with the command:  
# docker run datascience-notebook pytest /home/tests/jupyter_tests.py  
ENV TEST_DIR /home/tests/  
COPY tests/ /home/tests/  
  
RUN chmod +x /usr/local/bin/start-notebook.sh  

