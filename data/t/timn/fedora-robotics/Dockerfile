FROM fedora:25  
MAINTAINER Tim Niemueller <niemueller@kbsg.rwth-aachen.de>  
  
# Disable Delta RPM, since docs are stripped doesn't work  
RUN echo "deltarpm=0" >> /etc/dnf/dnf.conf && \  
# Update and clean cache afterwards  
dnf -y update && dnf clean all  
  
# Install robotics related dependencies, be generous  
# Not in docker: ccache  
RUN dnf install -y \  
@buildsys-build @development-tools \  
gcc-c++ git make cmake hostname \  
doxygen asciidoc docbook-style-xsl texlive-dvips texlive-latex \  
kernel-headers elfutils-libelf-devel file-devel \  
yaml-cpp-devel PyYAML tinyxml-devel libxslt xmlrpc-c-devel \  
libxml2-devel libxml++-devel python3-libxml2 apr-util-devel \  
boost-devel log4cxx-devel poco-devel readline-devel bzip2-devel \  
gperftools-devel gtest-devel libtool-ltdl-devel sqlite-devel \  
tbb-devel python-setuptools numpy PyOpenGL \  
avahi-devel bluez-libs-devel libmicrohttpd-devel libdaemon-devel \  
openssl-devel libmodbus-devel \  
libjpeg-devel libpng-devel opencv-devel orocos-kdl-devel \  
libusb-devel hokuyoaist-devel libdc1394-devel libkni3-devel \  
libudev-devel urg-devel libkindrv-devel \  
festival festival-devel flite-devel \  
urdfdom-headers-devel urdfdom-devel \  
bullet-devel CGAL-devel eigen3-devel \  
gts-devel libccd-devel pcl-devel player-devel openni-devel \  
protobuf-devel protobuf-compiler \  
graphviz graphviz-devel rrdtool-devel \  
mongo-cxx-driver-devel mongodb-server \  
assimp-devel freeimage-devel ogre-devel \  
mesa-libGL-devel mesa-libGLU-devel freeglut-devel \  
libXext-devel qt-devel PyQt4-devel fltk-devel \  
SDL-devel SDL_image-devel SDL_net-devel \  
cairomm gconfmm26-devel glibmm24-devel gtkmm24-devel \  
gazebo-devel gazebo-ode-devel gazebo-media \  
\  
ros-release python-rospkg python3-rospkg console-bridge-devel \  
rospack rospack-devel python-rosdistro python-rosinstall \  
python-rosinstall_generator python-wstool python-rosdep python-rosdistro \  
python3-rosinstall_generator python3-rosinstall \  
python-qt5-devel python3-qt5-devel python2-defusedxml \  
sip-devel PyQt4-devel \  
python-netifaces \  
clips clipsmm-devel clips-emacs \  
compat-lua compat-lua-devel compat-tolua++-devel \  
collada-dom-devel python-collada python-empy lz4-devel libuuid-devel \  
screen \  
&& dnf clean all  
  

