##############################################################################################  
# Purpose : Dockerize Components of Pulsar software stack.  
# Python : 2.7  
# Version : 0.1  
# Author : Rob Lyon (robert.lyon@manchester.ac.uk)  
##############################################################################################  
# Based upon original script written by Casey Law (caseyjlaw@gmail.com) and  
# Maciej Serylak (mserylak@ska.ac.za).  
#  
# This docker file will setup an environment with only a basic pulsar stack.
This  
# is because the image is to be used for test vector generation, for tests of
SKA  
# SDP and CSP software. For a more complete pulsar image, look at the
Dockerfile's  
# written by Casey Law, or Maciej Serylak. I've documented this Dockerfile
which I  
# hope makes its content a lot easier to understand.  
#  
# SOFTWARE:  
#  
# psarchive  
# tempo2  
# fast_fake  
# inject_pulsar  
# pgplot  
# python 2.6 (scipy, numpy stacks).  
# fftw  
# dev tools (gfortran etc.)  
##############################################################################################  
# Use well supported Ubuntu distribution. Note that a newer version of Ubunutu  
# is available (16.04.1). See the docker site for more information.  
FROM ubuntu:14.04.4  
# Contact me for help!  
MAINTAINER robert.lyon@manchester.ac.uk  
  
# The WORKDIR instruction sets the working directory for any RUN, CMD,
ENTRYPOINT,  
# COPY and ADD instructions that follow it in the Dockerfile. If the WORKDIR
doesn’t  
# exist, it will be created even if it’s not used in any subsequent Dockerfile
instruction.  
WORKDIR /home  
  
# As part of its operation, the Apt tool uses a file that lists the 'sources'
from which  
# sofotware packages can be obtained. This file can be found at:
/etc/apt/sources.list.  
# The call below simply updates the sources file, so that software not
licensed under the  
# GPL (or similar license) can be downloaded via Apt to the image.  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse' >>
/etc/apt/sources.list  
  
##############################################################################################  
# Install 'OS' software.  
##############################################################################################  
  
# According to the docker reference documentation, which can be found online
at:  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/  
#  
# You should avoid RUN apt-get upgrade or dist-upgrade, as many of the
“essential” packages from  
# the base images won’t upgrade inside an unprivileged container. If you know
there’s a particular  
# package, foo, that needs to be updated, use apt-get install -y foo to update
automatically. The  
# documentation suggests that you should always combine RUN apt-get update,
with apt-get install  
# in the same RUN statement. We do this below to install the main software
packages we require.  
# Note that the -y flag used below causes Apt to responde with an automatic
yes to prompts. This  
# allows the commands to run non-interactively.  
RUN apt-get update -y && apt-get install -y \  
bc \  
autoconf \  
automake \  
autotools-dev \  
bison \  
build-essential \  
cmake \  
cmake-data \  
cmake-curses-gui \  
cpp \  
csh \  
cvs \  
cython \  
dkms \  
f2c \  
fftw2 \  
fftw-dev \  
flex \  
fort77 \  
gcc \  
g++ \  
gfortran \  
ghostscript \  
ghostscript-x \  
git \  
git-core \  
gnuplot \  
gnuplot-x11 \  
gsl-bin \  
gv \  
h5utils \  
hdf5-tools \  
htop \  
hdfview \  
hwloc \  
ipython \  
ipython-notebook \  
libbison-dev \  
libboost1.55-all-dev \  
libboost1.55-dev \  
libboost1.55-tools-dev \  
libc6-dev \  
libc-dev-bin \  
libcfitsio3 \  
libcfitsio3-dev \  
libcloog-isl4 \  
libcppunit-dev \  
libcppunit-subunit0 \  
libcppunit-subunit-dev \  
libfftw3-bin \  
libfftw3-dbg \  
libfftw3-dev \  
libfftw3-double3 \  
libfftw3-long3 \  
libfftw3-quad3 \  
libfftw3-single3 \  
libgd2-xpm-dev \  
libgd3 \  
libglib2.0-dev \  
libgmp3-dev \  
libgsl0-dev \  
libgsl0ldbl \  
libhdf5-7 \  
libhdf5-dev \  
libhdf5-serial-dev \  
libhwloc-dev \  
liblapack3 \  
liblapack3gf \  
liblapack-dev \  
liblapacke \  
liblapacke-dev \  
liblapack-pic \  
liblapack-test \  
libblas3 \  
libblas3gf \  
libblas-dev \  
liblua5.1-0 \  
liblua5.2-0 \  
libltdl7 \  
libltdl-dev \  
libncurses5-dev \  
libpng12-dev \  
libpng3 \  
libpng++-dev \  
libpth-dev \  
libreadline6 \  
libreadline6-dev \  
libsocket++1 \  
libsocket++-dev \  
libtool \  
libx11-dev \  
locate \  
lsof \  
m4 \  
make \  
man \  
mc \  
nano \  
nfs-common \  
numactl \  
openssh-server \  
pbzip2 \  
pgplot5 \  
pkgconf \  
pkg-config \  
python-qt4-dev \  
pyqt4-dev-tools \  
vim \  
wget \  
screen \  
subversion \  
swig \  
swig2.0 \  
tcsh \  
tk \  
tk-dev \  
tmux \  
python-pip \  
ca-certificates \  
curl  
  
#build-essential \  
#autoconf \  
#libtool \  
#csh \  
#git \  
#cvs \  
#fort77 \  
#gcc \  
#g++ \  
#gfortran \  
#wget  
# Install python modules  
RUN pip install pip -U && \  
pip install setuptools -U && \  
pip install numpy -U && \  
pip install scipy -U && \  
pip install fitsio -U && \  
pip install astropy -U && \  
pip install astroplan -U && \  
pip install pyfits -U && \  
pip install matplotlib -U && \  
pip install pyephem -U  
  
##############################################################################################  
# Setup environment variables  
##############################################################################################  
  
ENV PSRHOME=/home/psr/soft  
  
# Make the directory where software will be installed. Note the -p flag tells
mkdir to  
# also create parent directories as required.  
RUN mkdir -p /home/psr/soft  
# Define home, psrhome, software, OSTYPE  
ENV HOME=/home  
ENV OSTYPE=linux  
  
# Python packages  
ENV PYTHONPATH=$HOME/ve/lib/python2.7/site-packages  
  
  
# PGPLOT  
ENV PGPLOT_DIR=/usr/lib/pgplot5  
ENV PGPLOT_FONT=/usr/lib/pgplot5/grfont.dat  
ENV PGPLOT_INCLUDES=/usr/include  
ENV PGPLOT_BACKGROUND=white  
ENV PGPLOT_FOREGROUND=black  
ENV PGPLOT_DEV=/xs  
  
  
# calceph  
ENV PATH=$PATH:$PSRHOME/calceph-2.2.4/install/bin  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PSRHOME/calceph-2.2.4/install/lib  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$PSRHOME/calceph-2.2.4/install/include  
# ds9  
ENV PATH=$PATH:$PSRHOME/ds9-7.4  
# fv  
ENV PATH=$PATH:$PSRHOME/fv5.4  
# psrcat  
ENV PSRCAT_FILE=$PSRHOME/psrcat_tar/psrcat.db  
ENV PATH=$PATH:$PSRHOME/psrcat_tar  
  
  
# tempo  
ENV TEMPO=$PSRHOME/tempo  
ENV PATH=$PATH:$PSRHOME/tempo/bin  
  
  
# tempo2  
ENV TEMPO2=$PSRHOME/tempo2/T2runtime  
ENV PATH=$PATH:$PSRHOME/tempo2/T2runtime/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$PSRHOME/tempo2/T2runtime/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PSRHOME/tempo2/T2runtime/lib  
# PSRCHIVE  
ENV PSRCHIVE=$PSRHOME/psrchive  
ENV PATH=$PATH:$PSRCHIVE/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$PSRCHIVE/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PSRCHIVE/install/lib  
ENV PYTHONPATH=$PYTHONPATH:$PSRCHIVE/install/lib/python2.7/site-packages  
# SOFA C-library  
ENV SOFA=$PSRHOME/sofa  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$SOFA/20160503/c/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$SOFA/20160503/c/install/lib  
# SOFA FORTRAN-library  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$SOFA/20160503/f77/install/lib  
# SIGPROC  
# These flags assist with the Sigproc comilation process, so do not remove
them. If you take  
# them out, then Sigproc will not build correctly.  
ENV SIGPROC=$PSRHOME/sigproc  
ENV PATH=$PATH:$SIGPROC/install/bin  
ENV FC=gfortran  
ENV F77=gfortran  
ENV CC=gcc  
ENV CXX=g++  
  
  
# sigpyproc  
ENV SIGPYPROC=$PSRHOME/sigpyproc  
ENV PYTHONPATH=$PYTHONPATH:$SIGPYPROC/lib/python  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$SIGPYPROC/lib/c  
# CUB  
ENV CUB=$PSRHOME:cub-1.5.2  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH/$CUB  
  
  
# PSRDADA  
ENV PSRDADA=$PSRHOME/psrdada  
ENV PATH=$PATH:$PSRDADA/install/bin  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PSRDADA/install/lib  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$PSRDADA/install/include  
ENV CUDA_NVCC_FLAGS="-O3 -arch sm_30 -m64 -lineinfo -I$PSRHOME/cub-1.5.2"  
# szlib  
ENV SZIP=$PSRHOME/szip-2.1  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$SZIP/install/lib  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$SZIP/install/include  
# h5check  
ENV H5CHECK=$PSRHOME/h5check-2.0.1  
ENV PATH=$PATH:$H5CHECK/install/bin  
  
  
# DAL  
ENV DAL=$PSRHOME/DAL  
ENV PATH=$PATH:$DAL/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$DAL/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DAL/install/lib  
# DSPSR  
ENV DSPSR=$PSRHOME/dspsr  
ENV PATH=$PATH:$DSPSR/install/bin  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DSPSR/install/lib  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$DSPSR/install/include  
# clig  
ENV CLIG=$PSRHOME/clig  
ENV PATH=$PATH:$CLIG/instal/bin  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CLIG/instal/lib  
# CLooG  
ENV CLOOG=$PSRHOME/cloog-0.18.4  
ENV PATH=$PATH:$CLOOG/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$CLOOG/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CLOOG/install/lib  
# Ctags  
ENV CTAGS=$PSRHOME/ctags-5.8  
ENV PATH=$PATH:$CTAGS/install/bin  
  
  
# GeographicLib  
ENV GEOLIB=$PSRHOME/GeographicLib-1.46  
ENV PATH=$PATH:$GEOLIB/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$GEOLIB/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$GEOLIB/install/lib  
ENV PYTHONPATH=$PYTHONPATH:$GEOLIB/install/lib/python/site-packages  
# h5edit  
ENV H5EDIT=$PSRHOME/h5edit-1.3.1  
ENV PATH=$PATH:$H5EDIT/install/bin  
  
  
# Leptonica  
ENV LEPTONICA=$PSRHOME/leptonica-1.73  
ENV PATH=$PATH:$LEPTONICA/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$LEPTONICA/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LEPTONICA/install/lib  
# tvmet  
ENV TVMET=$PSRHOME/tvmet-1.7.2  
ENV PATH=$PATH:$TVMET/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$TVMET/install/include  
# FFTW2  
ENV FFTW2=$PSRHOME/fftw-2.1.5  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$FFTW2/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$FFTW2/install/lib  
# fitsverify  
ENV FITSVERIFY=$PSRHOME/fitsverify  
ENV PATH=$PATH:$FITSVERIFY  
  
  
# PSRSALSA  
ENV PSRSALSA=$PSRHOME/psrsalsa  
ENV PATH=$PATH:$PSRSALSA/bin  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PSRSALSA/src/lib  
# pypsrfits  
ENV PYPSRFITS=$PSRHOME/pypsrfits  
  
  
# PRESTO  
ENV PRESTO=$PSRHOME/presto  
ENV PATH=$PATH:$PRESTO/bin  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PRESTO/lib  
ENV PYTHONPATH=$PYTHONPATH:$PRESTO/lib/python  
# wapp2psrfits  
ENV WAPP2PSRFITS=$PSRHOME/wapp2psrfits  
ENV PATH=$PATH:$WAPP2PSRFITS  
  
  
# psrfits2psrfits  
ENV PSRFITS2PSRFITS=$PSRHOME/psrfits2psrfits  
ENV PATH=$PATH:$PSRFITS2PSRFITS  
  
  
# psrfits_utils  
ENV PSRFITS_UTILS=$PSRHOME/psrfits_utils  
ENV PATH=$PATH:$PSRFITS_UTILS/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$PSRFITS_UTILS/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$PSRFITS_UTILS/install/lib  
# pyslalib  
ENV PYSLALIB=$PSRHOME/pyslalib  
ENV VPSR=$PSRHOME/Vpsr  
  
  
# Vpsr  
ENV PATH=$PATH:$VPSR  
  
  
# GPy  
ENV GPY=$PSRHOME/GPy  
ENV PATH=$PATH:$GPY  
  
  
# katversion  
ENV KATVERSION=$PSRHOME/katversion  
  
  
# katpoint  
ENV KATPOINT=$PSRHOME/katpoint  
  
  
# katdal  
ENV KATDAL=$PSRHOME/katdal  
  
  
# katconfig  
ENV KATCONFIG=$PSRHOME/katconfig  
  
  
# katsdpscripts  
ENV KATSDPSCRIPTS=$PSRHOME/katsdpscripts  
  
  
# katsdpinfrastructure  
ENV KATSDPINFRASTRUCTURE=$PSRHOME/katsdpinfrastructure  
  
  
# katpulse  
ENV KATPULSE=$PSRHOME/katpulse  
  
  
# casacore measures_data  
ENV MEASURES_DATA=$PSRHOME/measures_data  
  
  
# casa  
ENV CASA=$PSRHOME/casa-release-4.6.0-el6  
ENV PATH=$PATH:$PSRHOME/casa-release-4.6.0-el6/bin  
  
  
# casacore  
ENV CASACORE=$PSRHOME/casacore  
ENV PATH=$PATH:$CASACORE/build/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$CASACORE/build/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CASACORE/build/install/lib  
# python-casacore  
ENV PYTHON_CASACORE=$PSRHOME/python-casacore  
  
  
# makems  
ENV MAKEMS=$PSRHOME/makems  
ENV PATH=$PATH:$MAKEMS/LOFAR/installed/gnu_opt/bin  
ENV
C_INCLUDE_PATH=$C_INCLUDE_PATH:$MAKEMS/LOFAR/installed/gnu_opt/LOFAR/installed/gnu_opt/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$MAKEMS/LOFAR/installed/gnu_opt/lib64  
  
  
# wsclean  
ENV WSCLEAN=$PSRHOME/wsclean-1.12  
ENV PATH=$PATH:$WSCLEAN/build/install/bin  
ENV C_INCLUDE_PATH=$C_INCLUDE_PATH:$WSCLEAN/build/install/include  
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$WSCLEAN/build/install/lib  
# coast_guard  
ENV COAST_GUARD=$PSRHOME/coast_guard  
ENV PATH=$PATH:$COAST_GUARD  
ENV COASTGUARD_CFG=$COAST_GUARD/configurations  
ENV PYTHONPATH=$PYTHONPATH:$COAST_GUARD  
  
# Downloading all source codes  
RUN git clone https://github.com/SixByNine/sigproc.git  
RUN git clone https://github.com/scottransom/presto.git  
RUN git clone git://git.code.sf.net/p/tempo/tempo  
RUN mv /home/sigproc /home/psr/soft/sigproc  
RUN mv /home/presto /home/psr/soft/presto  
RUN mv /home/tempo /home/psr/soft/tempo  
RUN cvs -z3 -d:pserver:anonymous@tempo2.cvs.sourceforge.net:/cvsroot/tempo2 co
tempo2  
RUN mv /home/tempo2 /home/psr/soft/tempo2  
  
  
##############################################################################################  
# CUDA Drivers  
#  
# This part of the docker file was taken from the Nvidia Github respository,
credit goes  
# to the NVIDIA CORPORATION <digits@nvidia.com> for this. Please see the
following link  
# for more information: https://github.com/NVIDIA/nvidia-docker  
##############################################################################################  
  
ENV CUDA_VERSION 8.0  
LABEL com.nvidia.cuda.version="8.0"  
  
ENV CUDA_DOWNLOAD_SUM
58a5f8e6e8bf6515c55fd99e38b1a617142e556c70679cf563f30f972bbdd811  
  
ENV CUDA_PKG_VERSION 8-0=8.0.27-1  
RUN curl -o cuda-repo.deb -fsSL
http://developer.download.nvidia.com/compute/cuda/8.0/direct/cuda-repo-
ubuntu1404-8-0-rc_8.0.27-1_amd64.deb && \  
echo "$CUDA_DOWNLOAD_SUM cuda-repo.deb" | sha256sum -c --strict - && \  
dpkg -i cuda-repo.deb && \  
rm cuda-repo.deb && \  
apt-get update && apt-get install -y --no-install-recommends \  
cuda-nvrtc-$CUDA_PKG_VERSION \  
cuda-nvgraph-$CUDA_PKG_VERSION \  
cuda-cusolver-$CUDA_PKG_VERSION \  
cuda-cublas-$CUDA_PKG_VERSION \  
cuda-cufft-$CUDA_PKG_VERSION \  
cuda-curand-$CUDA_PKG_VERSION \  
cuda-cusparse-$CUDA_PKG_VERSION \  
cuda-npp-$CUDA_PKG_VERSION \  
cuda-cudart-$CUDA_PKG_VERSION && \  
ln -s cuda-$CUDA_VERSION /usr/local/cuda && \  
apt-get remove --purge -y cuda-repo-ubuntu1404-8-0-rc && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "/usr/local/cuda/lib" >> /etc/ld.so.conf.d/cuda.conf && \  
echo "/usr/local/cuda/lib64" >> /etc/ld.so.conf.d/cuda.conf && \  
ldconfig  
  
RUN echo "/usr/local/nvidia/lib" >> /etc/ld.so.conf.d/nvidia.conf && \  
echo "/usr/local/nvidia/lib64" >> /etc/ld.so.conf.d/nvidia.conf  
  
ENV PATH /usr/local/nvidia/bin:/usr/local/cuda/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
##############################################################################################  
# TEST VECTOR PIPELINE + README Setup  
##############################################################################################  
# Download test vector files  
WORKDIR /home  
RUN wget
https://github.com/scienceguyrob/Docker/raw/master/Resources/Deploy/DockerImageReadme.txt  
  
WORKDIR $PSRHOME  
RUN wget
https://github.com/scienceguyrob/Docker/raw/master/Resources/Deploy/pulsar_injection_pipeline.zip  
RUN unzip pulsar_injection_pipeline.zip -d $PSRHOME  
RUN rm __MACOSX -R  
RUN rm pulsar_injection_pipeline.zip  
  
##############################################################################################  
# Elmarie van Heerden's Code  
##############################################################################################  
  
RUN mkdir /home/psr/soft/evh  
WORKDIR $PSRHOME/evh  
RUN wget
https://raw.githubusercontent.com/EllieVanH/PulsarDetectionLibrary/master/README.txt  
RUN wget
https://raw.githubusercontent.com/EllieVanH/PulsarDetectionLibrary/master/ersatz.py  
  
##############################################################################################  
# TEMPO Installation  
##############################################################################################  
WORKDIR $PSRHOME/tempo  
RUN ./prepare && \  
./configure --prefix=$PSRHOME/tempo && \  
make && \  
make install && \  
mv obsys.dat obsys.dat_ORIGINAL && \  
wget https://raw.githubusercontent.com/mserylak/pulsar_docker/master/obsys.dat  
  
##############################################################################################  
# TEMPO2 Installation  
##############################################################################################  
# Ok here we install the latest version of TEMPO2.  
  
WORKDIR $PSRHOME/tempo2  
RUN sync && perl -pi -e 's/chmod \\+x/#chmod +x/' bootstrap # Get rid of:
returned a non-zero code: 126.  
RUN ./bootstrap && \  
./configure --x-libraries=/usr/lib/x86_64-linux-gnu --enable-shared --enable-
static --with-pic F77=gfortran && \  
make && \  
make install && \  
make plugins-install  
WORKDIR $PSRHOME/tempo2/T2runtime/observatory  
RUN mv observatories.dat observatories.dat_ORIGINAL && \  
mv oldcodes.dat oldcodes.dat_ORIGINAL && \  
mv aliases aliases_ORIGINAL && \  
wget
https://raw.githubusercontent.com/mserylak/pulsar_docker/master/observatories.dat
&& \  
wget
https://raw.githubusercontent.com/mserylak/pulsar_docker/master/oldcodes.dat
&& \  
wget https://raw.githubusercontent.com/mserylak/pulsar_docker/master/aliases  
  
##############################################################################################  
# Sigproc Installation  
##############################################################################################  
# Ok here we install sigproc - This is Mike Keith's version of Sigproc, which
comes with the  
# fast_fake utility. First we set the environment variables for the install,
then execute the  
# building steps.  
WORKDIR $SIGPROC  
RUN ./bootstrap && \  
./configure --prefix=$SIGPROC/install
LDFLAGS="-L/home/psr/soft/tempo2/T2runtime/lib" LIBS="-ltempo2" && \  
make && \  
make install  
  
##############################################################################################  
# PRESTO Installation  
##############################################################################################  
WORKDIR $PRESTO/src  
#RUN make makewisdom  
RUN make prep && \  
make  
WORKDIR $PRESTO/python/ppgplot_src  
RUN mv _ppgplot.c _ppgplot.c_ORIGINAL && \  
wget
https://raw.githubusercontent.com/mserylak/pulsar_docker/master/_ppgplot.c  
WORKDIR $PRESTO/python  
RUN make  
  
##############################################################################################  
# Finally...  
##############################################################################################  
# Define the command that will be exectuted when docker runs the container.  
WORKDIR /home  
ENTRYPOINT /bin/bash

