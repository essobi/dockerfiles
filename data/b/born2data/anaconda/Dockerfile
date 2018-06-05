FROM debian:jessie  
MAINTAINER Jonathan DEKHTIAR "contact@jonathandekhtiar.eu"  
# Link in our build files to the docker image  
ADD src/ /tmp  
  
# Run all ubuntu updates and apt-get installs  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get upgrade -y --fix-missing && \  
apt-get install -y --fix-missing git \  
wget \  
build-essential \  
python-dev \  
sudo \  
vim \  
libglu-dev \  
libgl1-mesa-dev \  
libxtst6 \  
libxt-dev \  
libxt6 \  
libglib2.0-0 \  
&& apt-get clean  
  
# Run all python installs  
# Perform any cleanup of the install as needed  
# Copy notebook config into ipython directory  
# Make sure our user owns the directory  
RUN /tmp/install.sh && \  
apt-get \--purge -y autoremove wget && \  
cp /tmp/ipython_notebook_config.py /home/condauser/.ipython/profile_default/
&& \  
cp /tmp/matplotlib_nb_init.py /home/condauser/.ipython/profile_default/startup
&& \  
chown condauser:condauser /home/condauser -R  
  
# Set persistent environment variables for python3 and python2  
ENV PY2PATH=/home/condauser/anaconda3/envs/python2/bin  
ENV PY3PATH=/home/condauser/anaconda3/bin  
  
# Install the python2 ipython kernel  
RUN $PY2PATH/python $PY2PATH/ipython kernelspec install-self  
  
RUN chmod +x /tmp/packageInstall.sh  
RUN /tmp/packageInstall.sh  
  
# Setup our environment for running the ipython notebook  
EXPOSE 8888  
USER condauser  
ENV HOME=/home/condauser  
ENV SHELL=/bin/bash  
ENV USER=condauser  
WORKDIR /home/condauser/notebooks  
  
CMD $PY3PATH/ipython notebook  
  
  
sudo apt-get install libfontconfig1 libXrender1 libsm6 libfreetype6
libglib2.0-0 libgtk2.0-0 libgtk2.0-0 libgdk-pixbuf2.0-0 libfontconfig1
libxrender1 libx11-6 libglib2.0-0 libxft2 libfreetype6 libc6 zlib1g libpng12-0
libgcc1  
apt-get install x11-xserver-utils

