FROM magicvisionlab/mvllinux-base  
MAINTAINER ueck@net-labs.de  
ENV DEBIAN_FRONTEND noninteractive  
  
# LOCAL BUILD ONLY - USE AptProxy  
#RUN echo "Use Localhost as AptProxy http://"`netstat -nr | grep
'^0\\.0\\.0\\.0' | awk '{print $2}'`":3142"  
#RUN echo 'Acquire::http { Proxy "http://'`netstat -nr | grep '^0\\.0\\.0\\.0'
| awk '{print $2}'`':3142"; };' | sudo tee /etc/apt/apt.conf.d/02proxy  
# enable ubuntu multiverse  
RUN echo deb http://archive.ubuntu.com/ubuntu trusty multiverse >>
/etc/apt/sources.list && \  
echo deb-src http://archive.ubuntu.com/ubuntu trusty multiverse >>
/etc/apt/sources.list && \  
echo deb http://security.ubuntu.com/ubuntu trusty-security multiverse >>
/etc/apt/sources.list && \  
echo deb-src http://security.ubuntu.com/ubuntu trusty-security multiverse >>
/etc/apt/sources.list && \  
apt-get update  
  
# install x-windows subsystem  
RUN apt-get -y --force-yes install x-window-system && \  
apt-get install -y binutils && \  
apt-get install -y pkg-config && \  
apt-get install -y x11vnc && \  
apt-get install -y mesa-utils && \  
apt-get install -y libgtk2.0-0 && \  
apt-get install -y twm  
  
  
# install basic packages for magicvisionlab gui development  
RUN apt-get install -y \  
cmake-gui \  
libqt4-dev \  
libqt4-dev-bin \  
libqt4-opengl-dev \  
libqt4-qt3support \  
libqt4-sql-sqlite \  
libqtwebkit-dev \  
libopencv-dev \  
freeglut3-dev \  
libftgl-dev \  
libfreetype6-dev \  
libglew-dev \  
libglfw-dev \  
libwxgtk3.0-dev \  
libmotif-dev \  
libx11-dev \  
libxft-dev \  
libxi-dev \  
libxslt1-dev \  
mesa-common-dev \  
qtbase5-dev \  
qtbase5-dev-tools \  
libxmu-dev \  
libglade2-0 \  
libglademm-2.4-1c2a \  
libgtkmm-2.4-1c2a \  
libgtkglextmm-x11-1.2-dev  
  
# CLEANUP LOCAL PROXY  
#RUN rm -f /etc/apt/apt.conf.d/02proxy  

