#  
# Staphopia Analysis Pipeline Dockerfile  
#  
# https://github.com/staphopia/staphopia-docker  
#  
# Start with Ubuntu 16.04  
FROM ubuntu:16.04  
MAINTAINER rp3@staphopia.com  
  
# Install required programs  
RUN apt-get update -qq && apt-get install -y \  
bioperl \  
g++-4.9 \  
gcc-4.9 \  
git \  
libffi-dev \  
libncurses5-dev \  
libsqlite3-dev \  
libssl-dev \  
make \  
python-dev \  
python-numpy \  
python-pip \  
python-scipy \  
r-base \  
wget  
  
# Set default GCC to 4.9  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 60 \  
\--slave /usr/bin/g++ g++ /usr/bin/g++-4.9  
  
RUN pip install --upgrade pip  
RUN pip install --upgrade requests[security]  
  
# Install for Prokka  
RUN cpan install XML::Simple  
  
# Set up Staphopia  
RUN mkdir -p /staphopia/apps  
RUN useradd --create-home --shell /bin/bash staphopia  
RUN chown -R staphopia /staphopia  
USER staphopia  
RUN \  
cd /staphopia/apps && \  
git clone https://github.com/staphopia/staphopia-ap.git && \  
cd staphopia-ap && \  
make && \  
make docker-clean && \  
cd  
  
# export PATHS  
ENV PYTHONPATH /staphopia/apps/staphopia-ap/libs/python:$PYTHONPATH  
ENV PATH /staphopia/apps/staphopia-ap/bin:$PATH  
WORKDIR /data  
  
RUN echo 'git pull 0002' > /dev/null && cd /staphopia/apps/staphopia-ap && git
pull  

