FROM ubuntu:utopic  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# apt  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-get update  
  
# utils pkgs  
RUN apt-get install -y \  
git \  
openssh-client \  
pkg-config \  
unzip \  
wget  
  
# base pkgs  
RUN apt-get install -y \  
build-essential \  
libatlas-dev \  
libatlas3gf-base \  
libfreetype6-dev \  
libyaml-dev \  
pandoc  
  
# audio pkgs  
RUN apt-get install -y \  
libav-tools \  
libavcodec-dev \  
libavformat-dev \  
libavresample-dev \  
libavutil-dev \  
libfftw3-dev \  
libfftw3-doc \  
libsamplerate0-dev \  
libtag1-dev  
  
# python pkgs  
RUN apt-get install -y \  
cython \  
ipython-notebook \  
python-audioread \  
python-dev \  
python-nose \  
python-numpy \  
python-numpy-dev \  
python-pandas \  
python-pip \  
python-pygame \  
python-scipy \  
python-setuptools  
  
# dsp libs  
ADD bin/ bin/  
RUN bin/install-pips  
RUN bin/install-essentia  
RUN bin/install-sms-tools  
  
# configure  
EXPOSE 8888  
VOLUME ["/notebooks"]  
CMD ["bin/ipython"]  

