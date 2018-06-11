# 17.10 is the latest - Out on October, 2017  
#FROM ubuntu:17.10  
FROM ubuntu:16.04  
FROM python:3.6  
# Headless front-end, remove warnings  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Get most recent updates  
RUN apt-get update -qq  
  
# Install apt add repository and ffmpeg  
#RUN apt-get install -y software-properties-common  
#RUN add-apt-repository ppa:mc3man/trusty-media  
#RUN apt-get update  
#RUN apt update -qq && apt-get install -y apt-transport-https  
#RUN apt install ffmpeg libav-tools x264 x265  
# ffmpeg: https://stackoverflow.com/questions/42589892/how-to-install-ffmpeg-
for-ubuntu-using-command-line  
RUN apt-get -y update && apt-get install -y wget nano git build-essential yasm
pkg-config  
  
# Compile and install ffmpeg from source  
RUN git clone https://github.com/FFmpeg/FFmpeg /root/ffmpeg && \  
cd /root/ffmpeg && \  
./configure --enable-nonfree --disable-shared --extra-
cflags=-I/usr/local/include && \  
make -j8 && make install -j8  
  
# If you want to add some content to this image because the above takes a
LONGGG time to build  
ARG CACHEBREAK=1  
# Utils  
RUN apt-get install -y --no-install-recommends apt-utils \  
&& apt-get install -y --no-install-recommends \  
locales \  
ssh vim unzip less procps \  
git curl wget \  
build-essential g++ cmake \  
&& echo 'Acquire::Retries "5";' > /etc/apt/apt.conf.d/99AcquireRetries \  
&& sed -i 's/main$/main contrib non-free/' /etc/apt/sources.list  
##&& apt-get install -y --no-install-recommends linux-headers-generic
initramfs-tools  
# Locales  
ENV LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"  
# Python (3.5)  
# Aliases (but don't sym-link) python -> python3 and pip -> pip3  
RUN apt-get install -y --no-install-recommends \  
python3 \  
python3-dev \  
python3-pip \  
python3-setuptools \  
#python3-virtualenv \  
pkg-config \  
# Required for keras  
python3-h5py \  
python3-yaml \  
python3-pydot  
  
# Upgrade with latest pip and create aliases  
RUN pip3 install --no-cache-dir --upgrade pip setuptools \  
&& echo "alias python='python3'" >> /root/.bash_aliases \  
&& echo "alias pip='pip3'" >> /root/.bash_aliases  
  
## Python scientific libraries  
RUN pip3 --no-cache-dir install \  
numpy \  
scipy \  
scikit-learn \  
scikit-image \  
pydicom \  
h5py \  
django \  
imageio \  
sk-video \  
SimpleITK  
  
# Clean-up  
RUN apt-get clean && apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD . /USPro  
WORKDIR /USPro  
  
# Install imageio  
#RUN ["chmod", "+x", "/USPro/USApp/install_ffmpeg.py"]  
#RUN ["python","/USPro/USApp/install_ffmpeg.py"]  
LABEL maintainer="Adrian <adrian dot haimovich at yale dot edu>"  
  
EXPOSE 8000  
# Permissions for entrypoint script  
RUN ["chmod", "+x", "/USPro/docker_entrypoint.sh"]  
  
# Jupyter notebook  
#RUN pip3 --no-cache-dir install jupyter \  
# Jupyter config: don't open browser. Password will be set when launching, see
below.  
# && mkdir /root/.jupyter \  
# && echo "c.NotebookApp.ip = '*'" \  
# "\nc.NotebookApp.open_browser = False" \  
# > /root/.jupyter/jupyter_notebook_config.py  
#EXPOSE 8888  
# default password: keras  
#ENV PASSWD='sha1:98b767162d34:8da1bc3c75a0f29145769edc977375a373407824'  
#CMD jupyter notebook --allow-root --no-browser --ip=*
--NotebookApp.password="$PASSWD" \  
# & /bin/bash  
# Assign entrypoint script  
ENTRYPOINT ["/USPro/docker_entrypoint.sh"]  
  

