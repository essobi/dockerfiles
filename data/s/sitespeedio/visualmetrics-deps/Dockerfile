FROM sitespeedio/node:ubuntu-18.04-nodejs8.11.1  
# Lets install all dependencies for VisualMetrics  
RUN buildDeps='wget' && \  
apt-get update -y && apt-get install -y \  
imagemagick \  
ipython \  
libjpeg-dev \  
python \  
python-dev \  
python-pil \  
python-numpy \  
python-scipy \  
python-matplotlib \  
python-pandas \  
python-pip \  
python-sympy \  
python-nose \  
xz-utils \  
$buildDeps \  
\--no-install-recommends --force-yes && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/* && \  
python -m pip install --upgrade pip && \  
python -m pip install --upgrade setuptools && \  
python -m pip install pyssim && \  
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-
static.tar.xz && \  
tar --strip-components 1 -C /usr/bin -xf ffmpeg-release-64bit-static.tar.xz
--wildcards */ffmpeg */ffprobe && \  
rm ffmpeg-release-64bit-static.tar.xz && \  
apt-get purge -y --auto-remove $buildDeps \  

