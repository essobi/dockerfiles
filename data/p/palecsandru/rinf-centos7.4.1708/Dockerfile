FROM centos:centos7.4.1708  
  
  
###############################################################################  
# General update  
###############################################################################  
RUN yum update -y  
  
  
###############################################################################  
# Repositories  
###############################################################################  
# EPEL  
RUN yum --enablerepo=extras install epel-release -y  
  
# Python3  
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm  
  
# FFMPEG  
RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro  
RUN yum -y install http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-
release-0-5.el7.nux.noarch.rpm  
  
  
###############################################################################  
# System dependencies  
###############################################################################  
RUN yum update -y  
RUN yum groupinstall "Development tools" -y  
RUN yum install -y \  
autoconf \  
automake \  
atlas-devel \  
bc \  
binutils \  
blas-devel \  
boost \  
boost-devel \  
build-essential \  
cmake \  
cmake3 \  
expect \  
epel-release \  
ffmpeg \  
ffmpeg-devel \  
flex \  
freeglut-devel \  
freetype \  
freetype-devel \  
future \  
gcc-c++ \  
gcc \  
gettext \  
git \  
glibc-devel \  
glibc-devel.i686 \  
gtk2-devel \  
gmp-devel \  
hdf5-devel \  
htop \  
java-1.8.0-openjdk-devel \  
mpfr-devel \  
libmpc-devel \  
lapack-devel \  
lcms2-devel \  
libffi-devel \  
libgcc.i686 \  
libgfortran \  
libjpeg-devel \  
libjpeg-turbo-devel \  
libmpc-devel \  
libpng-devel \  
libraqm-devel \  
libsndfile \  
libSM \  
libtiff-devel \  
libtool \  
libwebp-devel \  
libXext \  
libXi-devel \  
libXmu-devel \  
make \  
mlocate \  
mpfr-devel \  
net-tools \  
numactl \  
numpy \  
ntp \  
openssh-clients \  
openssh-server \  
openssl-devel \  
openssl-libs \  
patch \  
perf \  
pkgconfig \  
python-devel \  
python-pip \  
python36u \  
screen \  
suitesparse-devel \  
sysstat \  
tbb-devel \  
tcl-devel \  
telnet \  
texinfo \  
tk-devel \  
tkinter \  
vim \  
wget \  
which \  
zlib-devel  
  
  
###############################################################################  
# Others  
###############################################################################  
RUN echo 'export JAVA_HOME=/usr/lib/jvm/jre-1.8.0-openjdk' >> ~/.bashrc; \  
echo 'export JRE_HOME=/usr/lib/jvm/jre' >> ~/.bashrc; \  
echo 'export PATH='"${PATH}":'$JAVA_HOME/bin' >> ~/.bashrc  
RUN rm -f /usr/bin/python3 ;\  
cp /usr/bin/python3.6 /usr/bin/python3  
  
  
###############################################################################  
# Install Python3 dependencies  
###############################################################################  
RUN python3 -m ensurepip; \  
python3 -m pip install --upgrade pip==9.0.3; \  
python3 -m pip install PyYAML==3.12; \  
python3 -m pip install Flask==0.12.2; \  
python3 -m pip install Flask-CORS==3.0.3; \  
python3 -m pip install requests  
  
  
###############################################################################  
# Install Python2 dependencies  
###############################################################################  
RUN python2 -m pip install --upgrade pip==9.0.3; \  
python2 -m pip install requests; \  
python2 -m pip install setuptools; \  
python2 -m pip install enum34; \  
python2 -m pip install futures; \  
python2 -m pip install 'grpcio>=1.1.3'; \  
python2 -m pip install numpy; \  
python2 -m pip install h5py; \  
python2 -m pip install kafka; \  
python2 -m pip install mock; \  
python2 -m pip install pexpect; \  
python2 -m pip install --pre 'protobuf>=3.0.0a3'; \  
python2 -m pip install pyspark; \  
python2 -m pip install python-Levenshtein; \  
python2 -m pip install python_speech_features; \  
python2 -m pip install PySoundFile; \  
python2 -m pip install psutil; \  
python2 -m pip install requests; \  
python2 -m pip install scipy; \  
python2 -m pip install scikit-learn; \  
python2 -m pip install six; \  
python2 -m pip install tqdm; \  
python2 -m pip install wheel; \  
python2 -m pip install matplotlib; \  
python2 -m pip install Pillow; \  
python2 -m pip install scikit-image; \  
python2 -m pip install opencv-python; \  
python2 -m pip install paramiko  

