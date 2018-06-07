# Base python 3.6 build, inspired by https://github.com/Pakebo/eb-docker-
django-simple  
# Debian "tretch" | Python 3.6  
FROM python:3.6  
MAINTAINER Ignazio Indovina (ignazio.indovina@digitalbridge.eu) and Mike
Corlett (mike.corlett@digitalbridge.eu)  
  
##############################################################################  
# Environment variables  
##############################################################################  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
##############################################################################  
# OS Updates and Python packages  
##############################################################################  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y  
  
##############################################################################  
# Add compilers and basic tools  
##############################################################################  
  
# Libs required for geospatial libraries on Debian...  
RUN apt-get -y install apt-utils binutils libproj-dev gdal-bin build-essential  
# Operational packages .....  
RUN apt-get -y install curl wget nano g++ vim libapache2-mod-wsgi  
  
##############################################################################  
# INSTALL OpenGL and Glut libraries  
##############################################################################  
RUN apt-get install -y freeglut3 freeglut3-dev  
  
##############################################################################  
# OpenCV Reqs + gtk libraries for highgui, HDF5 and libmemcached etc.  
##############################################################################  
  
RUN apt-get install --yes gcc libatlas-base-dev gfortran libeigen3-dev  
RUN apt-get install --yes libmemcached-dev  
RUN apt-get install --yes libjpeg-dev libjpeg62 zlib1g-dev libfreetype6
libfreetype6-dev  
  
RUN apt-get install --yes cmake pkg-config libtiff-dev libjasper-dev  
RUN apt-get install --yes libgtk2.0-dev libavcodec-dev libavformat-dev  
RUN apt-get install --yes libswscale-dev libv4l-dev libopencv-dev libhdf5-dev  
RUN apt-get install --yes libboost-python-dev  
RUN apt-get install --yes aptitude  
  
RUN apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-
dev libhdf5-serial-dev protobuf-compiler gfortran liblapack-dev  
RUN apt-get install -y python3-dev  
RUN apt-get install -y --no-install-recommends libboost-all-dev  
RUN apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev
libeigen3-dev  
RUN apt-get install -y python-numpy python-scipy python-dev python-pip python-
nose g++ libopenblas-dev git  
RUN apt-get install -y gtk2-engines-pixbuf  
RUN apt-get install -y python-opencv  
  
##############################################################################  
# Install numpy, scipy etc as they are pre-compiled so they install faster  
##############################################################################  
RUN apt-get install -y --only-upgrade python-requests  
RUN pip install --upgrade pip  
RUN pip install wheel  
  
ENV PIP_WHEEL_DIR=/wheelhouse  
ENV WHEELHOUSE=/wheelhouse  
ENV PIP_FIND_LINKS=/wheelhouse  
  
RUN pip wheel numpy  
RUN pip install numpy  
  
RUN pip wheel scipy  
RUN pip install scipy  
  
RUN pip wheel scikit-learn  
RUN pip install scikit-learn  
  
RUN pip wheel Cython  
RUN pip install Cython  
RUN pip wheel six  
RUN pip install six  
RUN pip wheel Pillow  
RUN pip install Pillow  
RUN pip wheel h5py  
RUN pip install h5py  
RUN pip wheel msgpack-python  
RUN pip install msgpack-python  
RUN pip wheel matplotlib  
RUN pip install matplotlib  
  
# No wheels  
RUN pip install scikit-image  
RUN pip install pyamg  

