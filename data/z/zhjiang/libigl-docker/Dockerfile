# Use an official Python runtime as a base image  
FROM python:3.5-slim  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
sudo \  
apt-utils  
  
# Rebuild cache  
RUN cd /var/lib/apt && \  
sudo mv lists lists.old && \  
sudo mkdir -p lists/partial && \  
sudo apt-get update && \  
cd ~  
  
# Set the locale  
############## BASIC DEPENDENCIES AND COMMON PKGs #####################  
# Install vim & nano  
RUN apt-get --assume-yes install vim  
RUN apt-get --assume-yes install nano  
  
# More basic dependencies and python3  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
autoconf \  
bzip2 \  
ca-certificates \  
clang \  
cmake \  
curl \  
git \  
libblas-dev \  
libfreetype6 \  
libfreetype6-dev \  
libgl1-mesa-dev \  
libglu1-mesa \  
libglu1-mesa-dev freeglut3-dev mesa-common-dev \  
libosmesa6-dev \  
libpng12-dev \  
libtool \  
libxcursor-dev \  
libxi6 \  
libxinerama-dev \  
libxrandr-dev \  
libxrender1 \  
libzmq3-dev \  
module-init-tools \  
openssh-server \  
pkg-config \  
python3 \  
python3-dev \  
python3-pip \  
rsync \  
screen \  
software-properties-common \  
unzip \  
x11-xserver-utils \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
RUN sudo pip3 --no-cache-dir install --upgrade \  
pip \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
Pillow \  
h5py \  
keras \  
virtualenv  
  
RUN python3 -m pip install ipykernel  
RUN python3 -m ipykernel install  
RUN ln -sf /usr/bin/python3 /usr/bin/python  
#######################################################################  
######################## LIBIGL #######################################  
  
  
RUN git clone --recursive -b DockerAccess
https://github.com/jiangzhongshi/libigl.git  
WORKDIR libigl/python  
RUN mkdir build  
WORKDIR ./build  
ENV CC /usr/bin/clang  
ENV CXX /usr/bin/clang++  
RUN cmake ../ && make -j2  
  
#######################################################################  
######################## Blender #######################################  
ENV BLENDER_MAJOR 2.78  
ENV BLENDER_VERSION 2.78  
ENV BLENDER_BZ2_URL
http://download.blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-
linux-glibc219-x86_64.tar.bz2  
  
RUN mkdir /usr/local/blender \  
&& curl -SL "$BLENDER_BZ2_URL" -o blender.tar.bz2 \  
&& tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1 \  
&& rm blender.tar.bz2  
  
#######################################################################  
######################## Jupyter #######################################  
# Let's config jupyter notebook and its port access:  
####COPY config/jupyter_notebook_config.py /home/$username/.jupyter/  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# Just add a little wrapper script.  
###RUN echo -e \\#\\!/bin/bash\\\njupyter notebook >
/home/$username/run_jupyter.sh  
# Make port 80 available to the world outside this container  
EXPOSE 6666  
# Define environment variable  
ENV NAME World  
  
# Run app.py when the container launches  
CMD ["/bin/bash"]  

