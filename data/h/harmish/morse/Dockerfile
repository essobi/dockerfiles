FROM ubuntu:14.04  
ARG morseb=1.4_STABLE  
  
RUN apt-get update && \  
# install dependencies  
apt-get install -y \  
build-essential \  
cmake \  
git \  
pkg-config \  
redis-server \  
wget \  
xvfb && \  
#  
# get bleder  
wget -O /tmp/blender.tar.bz2
http://download.blender.org/release/Blender2.77/blender-2.77a-linux-
glibc211-x86_64.tar.bz2 && \  
mkdir /blender && tar -jxf /tmp/blender.tar.bz2 -C /blender --strip-
components=1 && \  
#  
# install conda  
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O
/tmp/miniconda.sh && \  
bash /tmp/miniconda.sh -b -p /miniconda && \  
#  
# install morse from source  
git clone https://github.com/harmishhk/morse -b $morseb /tmp/morse && \  
mkdir /tmp/morse/build /morse && \  
cd /tmp/morse/build && cmake .. -DPYTHON_EXECUTABLE=/miniconda/bin/python
-DBUILD_ROS_SUPPORT=OFF -DCMAKE_INSTALL_PREFIX=/morse && make install && \  
ln -s /morse/lib/python*/site-packages/pymorse $(python -c "from
distutils.sysconfig import get_python_lib; print(get_python_lib())")/pymorse
&& \  
#  
# install morseweb  
git clone https://github.com/yarox/morseweb /morseweb && \  
/miniconda/bin/pip install --no-cache-dir -r /morseweb/requirements.txt && \  
#  
# clean-up  
rm -rf /morseweb/.git && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set-up morse  
ENV MORSE_ROOT /morse  
ENV MORSE_BLENDER /blender/blender  
ENV MORSE_RESOURCE_PATH /morse/  
ENV PATH /miniconda/bin:/morse/bin/:$PATH  
ENV PYTHONPATH /morse/install/$morseb/lib/python3/dist-packages:$PYTHONPATH  
ENV HEADLESS true  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["bash", "/entrypoint.sh"]  

