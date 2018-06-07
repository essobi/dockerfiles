#  
# eudaq Dockerfile  
# https://github.com/duartej/dockerfiles/eudaq  
#  
# Creates the environment to run the EUDAQ  
# framework  
#  
FROM ubuntu:16.04  
LABEL author="jorge.duarte.campderros@cern.ch" \  
version="0.1-alpha" \  
description="Docker image for EUDAQ framework"  
# Place at the directory  
WORKDIR /eudaq  
  
# Install all dependencies  
RUN apt-get update && apt-get -y install \  
openssh-server \  
qt5-default \  
git \  
cmake \  
libusb-dev \  
pkgconf \  
python \  
python-dev \  
python-numpy \  
vim \  
g++ \  
gcc \  
gfortran \  
binutils \  
libxpm4 \  
libxft2 \  
libtiff5 \  
libeigen3-dev \  
default-jdk \  
libgsl-dev \  
libxpm-dev \  
libxft-dev \  
libx11-dev \  
libxext-dev \  
subversion \  
sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
# ROOT  
RUN mkdir /rootfr \  
&& wget https://root.cern.ch/download/root_v6.10.02.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz -O /rootfr/root.v6.10.02.tar.gz \  
&& tar -xf /rootfr/root.v6.10.02.tar.gz -C /rootfr \  
&& rm -rf /rootfr/root.v6.10.02.tar.gz  
  
ENV ROOTSYS /rootfr/root  
# BE aware of the ROOT libraries  
ENV LD_LIBRARY_PATH /rootfr/root/lib  
ENV PYTHONPATH /rootfr/root/lib  
  
# download the code, checkout the release and compile  
# This will be used only for production!  
# For development case, the /eudaq/eudaq directory  
# is "bind" from the host computer  
RUN git clone https://github.com/eudaq/eudaq.git \  
&& cd eudaq \  
&& git checkout tags/v1.7.0 -b v1.7.0 \  
&& mkdir -p /eudaq/eudaq/extern/ZestSC1 \  
&& mkdir -p /eudaq/eudaq/extern/tlufirmware  
  
# COPY The needed files for the TLU  
COPY ZestSC1.tar.gz /eudaq/eudaq/extern/ZestSC1.tar.gz  
COPY tlufirmware.tar.gz /eudaq/eudaq/extern/tlufirmware.tar.gz  
  
# Untar files and continue with the compilation  
RUN cd /eudaq/eudaq \  
&& tar xzf extern/ZestSC1.tar.gz -C extern && rm extern/ZestSC1.tar.gz \  
&& tar xzf extern/tlufirmware.tar.gz -C extern && rm extern/tlufirmware.tar.gz
\  
&& mkdir -p build \  
&& cd build \  
&& cmake .. -DBUILD_tlu=ON -DBUILD_python=ON -DBUILD_ni=ON \  
&& make -j4 install  
# STOP ONLY FOR PRODUCTION  
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/eudaq/eudaq/lib"  
ENV PYTHONPATH="${PYTHONPATH}:/eudaq/eudaq/lib:/eudaq/eudaq/python"  
ENV PATH="${PATH}:/rootfr/root/bin:/eudaq/eudaq/bin"  
COPY initialize_service.sh /usr/bin/initialize_service.sh  
  
# ILCSOFT (for EUTelescope) and LCIO ===================  
ENV ILCSOFT /eudaq/ilcsoft  
ENV EUTELESCOPE ${ILCSOFT}/v01-19-02/Eutelescope/master/  
ENV EUDAQ /eudaq/eudaq  
ENV ILCSOFT_CMAKE_ENV ${ILCSOFT}/v01-19-02/ILCSoft.cmake.env.sh  
ENV MILLEPEDEII
${ILCSOFT}/v01-19-02/Eutelescope/master/external/millepede2/tags/V04-03-03  
ENV MILLEPEDEII_VERSION tags/V04-03-03  
ENV GEAR ${ILCOSFT}/v01-19-02/gear/v01-06-eutel-pre  
ENV MARLIN ${ILCSOFT}/v01-19-02/Marlin/v01-09  
ENV MARLIN_DLL
${EUTELESCOPE}/lib/libEutelescope.so:${EUTELESCOPE}/lib/libEutelProcessors.so:${EUTELESCOPE}/lib/libEutelReaders.so:${EUDAQ}/lib/libNativeReader.so:${MARLIN_DLL}  
ENV GBL ${ILCSOFT}/v01-19-02/GBL/V02-01-02  
ENV
PATH="${PATH}:${MARLIN}/bin:${MILLEPEDEII}:${EUTELESCOPE}/bin:${GEAR}/tools:${GEAR}/bin"  
ENV
LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:${EUTELESCOPE}/lib:${GEAR}/lib:${GBL}/lib"  
COPY release-standalone-tuned.cfg ${ILCSOFT}/release-standalone-tuned.cfg  
  
# ILCSOFT compilation  
RUN mkdir -p ${ILCSOFT} \  
&& git clone -b dev-base https://github.com/eutelescope/ilcinstall
$ILCSOFT/ilcinstall \  
&& cd ${ILCSOFT}/ilcinstall \  
&& ${ILCSOFT}/ilcinstall/ilcsoft-install -i -v ${ILCSOFT}/release-standalone-
tuned.cfg \  
&& mkdir -p ${EUTELESCOPE}/build && cd ${EUTELESCOPE}/build \  
&& cmake .. \  
&& make -j4 install  
# ILCSOFT (for EUTelescope) and LCIO: DONE ===================  
# Recompile eudaq with lcio and eutelescope  
RUN . ${ILCSOFT}/v01-19-02/Eutelescope/master/build_env.sh \  
&& cd /eudaq/eudaq/build \  
&& cmake .. -DBUILD_tlu=ON -DBUILD_python=ON -DBUILD_ni=ON -DUSE_LCIO=ON
-DBUILD_nreader=ON \  
&& make -j4 install  
  
# Create a couple of directories needed  
RUN mkdir -p /logs && mkdir -p /data  
# Add eudaquser, allow to call sudo without password  
RUN useradd -md /home/eudaquser -ms /bin/bash -G sudo eudaquser \  
&& echo "eudaquser:docker" | chpasswd \  
&& echo "eudaquser ALL=(ALL) NOPASSWD: ALL\n" >> /etc/sudoers  
# Give previously created folders ownership to the user  
RUN chown -R eudaquser:eudaquser /logs && chown -R eudaquser:eudaquser /data \  
&& chown -R eudaquser:eudaquser /eudaq  
#&& chown -R eudaquser:eudaquser ${ILCSOFT} && chown -R eudaquser:eudaquser
/eudaq/eudaq  
USER eudaquser  
  
ENTRYPOINT . ${ILCSOFT}/v01-19-02/Eutelescope/master/build_env.sh && /bin/bash
-i  

