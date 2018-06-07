#  
# TRACS Dockerfile  
# https://github.com/duartej/dockerfiles-tracs  
#  
# Creates the environment to run the TRACS  
# utility and toolkit  
#  
# Uses phusion base image (actually an ubuntu 16.04)  
# with some improvements in order to be used ubuntu  
# in docker (https://github.com/phusion/baseimage-docker)  
#  
# Build the image:  
# docker build -t duartej/tracs_v2 .  
FROM phusion/baseimage:0.10.1  
LABEL author="jorge.duarte.campderros@cern.ch" \  
version="0.1-alpha" \  
description="Docker image for refurbished TRACS-v2"  
# -- Update and get needed packages  
USER root  
RUN apt-get update \  
&& install_clean --install-recommends software-properties-common \  
&& add-apt-repository ppa:fenics-packages/fenics \  
&& apt-get update \  
&& install_clean fenics \  
&& install_clean --install-recommends \  
libdolfin-dev \  
libvtk5-qt4-dev \  
tcl-vtk \  
python-vtk \  
libvtk-java \  
vim \  
libxpm4 \  
libxft2 \  
libtiff5 \  
libtbb2 \  
wget \  
sudo  
  
# ROOT  
RUN mkdir /rootfr \  
&& wget https://root.cern.ch/download/root_v6.12.06.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz -O /rootfr/root.v6.12.06.tar.gz \  
&& tar -xf /rootfr/root.v6.12.06.tar.gz -C /rootfr \  
&& rm -rf /rootfr/root.v6.12.06.tar.gz  
  
# ROOT use  
ENV ROOTSYS /rootfr/root  
# BE aware of the ROOT libraries  
ENV LD_LIBRARY_PATH /rootfr/root/lib  
ENV PYTHONPATH /rootfr/root/lib  
  
# User, add it to sudoers  
RUN useradd -m -s /bin/bash -G sudo tracs \  
&& echo "tracs:docker" | chpasswd \  
&& echo "tracs ALL=(ALL) NOPASSWD: ALL\n" >> /etc/sudoers \  
&& cat /etc/sudoers \  
## && mkdir /etc/service/syslog-forwarder \  
## && touch /etc/service/syslog-forwarder/down \  
&& rm /etc/my_init.d/10_syslog-ng.init \  
&& ldconfig  
  
WORKDIR /home/tracs  
  
# Create the directory to place the code, it should be  
# linked here when run the container:  
# docker run -it --rm --mount type=bind,source=/home/tracks/code,\  
# target=HOST_CODE -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix${DISPLAY} \  
# --mount type=bind,source=/home/duarte/repos/tracs,target=/home/tracs/code
duartej/tracs_v2duartej/tracs_v2  
USER tracs  
RUN touch /home/tracs/.sudo_as_admin_successful && \  
mkdir /home/tracs/tracs-code  
VOLUME /home/tracs/tracs-code  
  
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/home/tracs/code/build/lib"  
ENV PYTHONPATH="${PYTHONPATH}:/home/tracs/code/build/python"  
ENV PATH="${PATH}:/rootfr/root/bin:/home/tracs/code/build/bin"  
USER root  
ENTRYPOINT ["/sbin/my_init","--
quiet","--","/sbin/setuser","tracs","/bin/bash","-l","-c"]  
CMD ["/bin/bash","-i"]  

