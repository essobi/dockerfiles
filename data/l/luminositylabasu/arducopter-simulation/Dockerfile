FROM ubuntu:16.04  
  
LABEL maintainer="taforres@asu.edu"  
# ubuntu deps  
RUN apt-get -y update && apt-get -y install \  
dos2unix \  
g++-4.7 \  
ccache \  
python-lxml \  
screen \  
xterm \  
gdb \  
pkgconf \  
git \  
libc6 \  
libgcc1 \  
gcc-4.9-base \  
libstdc++5 \  
libstdc++6 \  
g++ \  
python-pip \  
python-matplotlib \  
python-serial \  
python-wxgtk3.0 \  
python-scipy \  
python-opencv \  
python-numpy \  
python-empy \  
python-pyparsing \  
python-serial \  
python-argparse \  
openocd \  
flex \  
bison \  
libncurses5-dev \  
autoconf \  
texinfo \  
build-essential \  
libftdi-dev \  
libtool zlib1g-dev \  
zip \  
genromfs \  
cmake \  
libtool \  
libtool-bin \  
automake \  
autoconf \  
libexpat1-dev  
  
# python pip deps  
RUN pip install --upgrade pip && pip install --no-cache-dir \  
pymavlink \  
MAVProxy \  
droneapi \  
future \  
pexpect \  
pymavlink && \  
easy_install catkin_pkg  
  
RUN git clone git://github.com/tridge/jsbsim.git  
WORKDIR "/jsbsim"  
RUN ./autogen.sh --enable-libraries && make  
  
# add ardupilot  
WORKDIR /  
RUN git clone https://github.com/ArduPilot/ardupilot.git \  
&& cd ardupilot \  
&& git submodule update --init --recursive  
  
# setup environment  
RUN echo 'export PATH=$PATH:/jsbsim/src' >> /etc/profile && \  
echo 'export PATH=$PATH:/ardupilot/Tools/autotest' >> /etc/profile && \  
echo 'export PATH=/usr/lib/ccache:$PATH' >> /etc/profile && \  
echo 'export PYTHONPATH=/usr/local/lib/python2.7/site-packages:$PYTHONPATH' >>
/etc/profile  
  
# setup entrypoint  
WORKDIR ardupilot/ArduCopter  
RUN . /etc/profile && sim_vehicle.py -w  
# use tcp b/c udp with docker does not work well  
ENV OUT_OPTIONS "--out=tcpin:0.0.0.0:14559"  
# gps lat, long for Goldwater  
ENV SIM_OPTIONS "-l=Goldwater=33.4209891,-111.9306707,0,0"  
EXPOSE 14559  
ENTRYPOINT . /etc/profile && sim_vehicle.py $OUT_OPTIONS $SIM_OPTIONS  

