FROM ubuntu:16.04  
  
MAINTAINER Matteo Bachetti <matteo@matteobachetti.it>  
  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse' >>
/etc/apt/sources.list && \  
mkdir /var/run/sshd && \  
apt-get -y check && \  
apt-get -y update && \  
apt-get install -y apt-utils apt-transport-https software-properties-common
python-software-properties && \  
apt-get -y update --fix-missing && \  
apt-get -y update && apt-get install -y pgplot5 && \  
mv /etc/apt/sources.list /etc/apt/sources.list.bak && \  
cat /etc/apt/sources.list.bak | grep -v multiverse > /etc/apt/sources.list &&
\  
apt-get -y update && apt-get -y update  
  
  
RUN apt-get install -qq ftp \  
wget \  
csh \  
build-essential \  
gfortran \  
libpng12-dev \  
libgd2-xpm-dev \  
cvs \  
autoconf \  
automake \  
libtool \  
m4 \  
git \  
gsl-bin \  
libgsl0-dev \  
flex \  
bison \  
fort77 \  
libglib2.0-dev \  
gnuplot \  
gnuplot-x11 \  
python-dev \  
python-numpy \  
python-scipy \  
python-matplotlib \  
ipython \  
python-sympy \  
python-nose \  
swig \  
libltdl-dev \  
libltdl7 \  
dkms \  
htop \  
screen \  
xterm \  
emacs \  
gpicview \  
xpdf \  
cmake \  
default-jre \  
default-jdk \  
libblas3 \  
liblapack3 \  
libblas-dev \  
liblapack-dev \  
libxext-dev \  
libx11-dev \  
libopenmpi-dev \  
openmpi-bin \  
libhdf5-openmpi-dev \  
mpich \  
libmpich-dev \  
libhdf5-mpich-dev \  
sudo \  
imagemagick\  
libfftw3-3 \  
libfftw3-bin \  
libfftw3-dbg \  
libfftw3-dev \  
libfftw3-double3 \  
libfftw3-long3 \  
libfftw3-quad3 \  
libfftw3-single3 \  
libcfitsio-bin \  
libcfitsio-dev \  
libcfitsio-doc \  
libcfitsio2 \  
libcfitsio3-dev \  
pgplot5  
  
  
RUN apt-get clean  
  
RUN useradd -m pulsar && echo "pulsar:pulsar" | chpasswd && adduser pulsar
sudo  
  
USER pulsar  
  
COPY .bashrc /home/pulsar/.bashrc  
  
RUN cd /home/pulsar && pwd && id && . /home/pulsar/.bashrc && mkdir
pulsar_software && cd pulsar_software  
  
RUN cd /home/pulsar/pulsar_software && \  
wget -q
http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz && \  
mkdir psrcat_tar pgplot && \  
tar zxf psrcat_pkg.tar.gz -C /home/pulsar/pulsar_software/psrcat_tar --strip-
components=1 && \  
rm *.tar.gz  
  
RUN cd /home/pulsar/pulsar_software && \  
git clone https://bitbucket.org/psrsoft/tempo2.git && \  
git clone git://github.com/scottransom/presto.git && \  
git clone git://git.code.sf.net/p/psrchive/code psrchive && \  
git clone git://git.code.sf.net/p/tempo/tempo && \  
git clone git://git.code.sf.net/p/dspsr/code dspsr && \  
git clone https://github.com/SixByNine/sigproc.git  
  
ENV ASTROSOFT /home/pulsar/pulsar_software  
  
RUN cd /home/pulsar/pulsar_software && mkdir -p bin include lib  
  
RUN cd /home/pulsar/pulsar_software/psrcat_tar && /bin/bash -c "source makeit"
&& cp psrcat $ASTROSOFT/bin/  
  
#RUN cd /home/pulsar/pulsar_software/ && mkdir pgplot_build  
#  
#COPY pgplot_drivers.list
/home/pulsar/pulsar_software/pgplot_build/drivers.list  
#  
#COPY pgplot_makefile /home/pulsar/pulsar_software/pgplot_build/makefile  
#  
#COPY pgplot_grexec.f $ASTROSOFT/pgplot_build/grexec.f  
#  
#RUN cd $ASTROSOFT/pgplot_build && make > build.log && make clean > clean.log
&& make cpg > cpg.log && \  
# ld -shared -o libcpgplot.so --whole-archive libcpgplot.a  
#  
#ENV PGPLOT_DIR $ASTROSOFT/pgplot_build  

