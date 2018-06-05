# The MIT License (MIT)  
#  
# Copyright (c) 2016 CNRS  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
#  
# AUTHORS  
# Hervé Bredin (bredin@limsi.fr)  
FROM pyannote/base-scientific-python  
MAINTAINER Hervé Bredin <bredin@limsi.fr>  
  
# -- ffmpeg --  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
libass-dev \  
libfdk-aac-dev \  
libmp3lame-dev \  
libopus-dev \  
libtheora-dev \  
libvdpau-dev \  
libvorbis-dev \  
libvpx-dev \  
libx264-dev \  
yasm \  
nasm  
  
RUN mkdir /tmp/ffmpeg_sources \  
&& cd /tmp/ffmpeg_sources \  
&& wget http://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2 \  
&& tar xjvf ffmpeg-snapshot.tar.bz2 \  
&& rm ffmpeg-snapshot.tar.bz2 \  
&& cd ffmpeg \  
&& ./configure \  
\--enable-shared \  
\--enable-gpl \  
\--enable-libass \  
\--enable-libfdk-aac \  
\--enable-libfreetype \  
\--enable-libmp3lame \  
\--enable-libopus \  
\--enable-libtheora \  
\--enable-libvorbis \  
\--enable-libvpx \  
\--enable-libx264 \  
\--enable-nonfree \  
&& make \  
&& make install \  
&& make distclean \  
&& hash -r \  
&& rm -rf /tmp/ffmpeg_sources  
  
# # -- Yaafe --  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
libmpg123-dev \  
libsndfile1 \  
libsndfile1-dev \  
libhdf5-dev \  
libargtable2-0 \  
libargtable2-dev \  
libfftw3-3 \  
libfftw3-dev  
  
RUN pip install pytest  
  
RUN wget https://github.com/Yaafe/Yaafe/archive/v0.65.1.tar.gz && \  
tar xzvf v0.65.1.tar.gz && \  
cd Yaafe-0.65.1 && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local \  
-DCMAKE_INSTALL_PYTHON_PACKAGES=/usr/local/lib/python2.7/dist-packages \  
-DCMAKE_INSTALL_YAAFE_EXTENSIONS=/usr/local/lib/python2.7/dist-packages \  
-DWITH_FFTW3=ON \  
-DWITH_LAPACK=ON \  
-DWITH_MATLAB_MEX=OFF \  
-DWITH_MPG123=ON \  
-DWITH_SNDFILE=ON \  
-DWITH_HDF5=ON \  
.. && \  
make && \  
make install && \  
cd ../.. && \  
rm -rf Yaafe-0.65.1 v0.65.1.tar.gz  
  
ENV YAAFE_PATH /usr/local/lib/python2.7/dist-packages  

