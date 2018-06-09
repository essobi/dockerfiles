# Docker image for building and testing tkwant  
FROM ubuntu:16.04  
MAINTAINER Kwant developers <authors@kwant-project.org>  
  
# make our environment sane  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# all the hard non-Python dependencies  
git g++ make patch gfortran libblas-dev liblapack-dev \  
libmumps-scotch-dev pkg-config libfreetype6-dev \  
# all the hard Python dependencies  
python3-all-dev python3-setuptools python3-pip python3-tk python3-wheel \  
cython3 python3-numpy python3-scipy python3-matplotlib python3-sympy\  
# Additional tools for running CI  
file rsync openssh-client \  
# Doc-building tools  
inkscape texlive-full zip \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
### install build and testing dependencies  
RUN pip3 install -U pip  
RUN pip3 install \  
"cython>=0.25.1" \  
"pytest>=3"\  
"pytest-runner>=2.7" \  
pytest-cov \  
pytest-flakes \  
pytest-pep8 \  
"nose>=1.0"\  
nose-cov \  
"sphinx>=1.5.1,<1.6" \  
"requests>=2.12.4" \  
numpydoc \  
tinyarray>=1.2.0 \  
matplotlib>=2.0  

