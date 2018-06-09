# Copyright (C) 2016 by Ewan Barr  
# Licensed under the Academic Free License version 3.0  
# This program comes with ABSOLUTELY NO WARRANTY.  
# You are free to modify and redistribute this code as long  
# as you do not remove the above attribution and reasonably  
# inform receipients that you have modified the original work.  
FROM ubuntu:16.04  
MAINTAINER Ewan Barr "ebarr@mpifr-bonn.mpg.de"  
# Suppress debconf warnings  
ENV DEBIAN_FRONTEND noninteractive  
  
# Switch account to root and adding user accounts and password  
USER root  
RUN echo "root:root" | chpasswd && \  
mkdir -p /root/.ssh  
  
# Create psr user which will be used to run commands with reduced privileges.  
RUN adduser --disabled-password --gecos 'unprivileged user' psr && \  
echo "psr:psr" | chpasswd && \  
mkdir -p /home/psr/.ssh && \  
chown -R psr:psr /home/psr/.ssh  
  
# Create space for ssh daemon and update the system  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu trusty main multiverse' >>
/etc/apt/sources.list && \  
mkdir /var/run/sshd && \  
apt-get -y check && \  
apt-get -y update && \  
apt-get install -y apt-utils apt-transport-https software-properties-common
python-software-properties && \  
apt-get -y update --fix-missing && \  
apt-get -y upgrade  
  
# Install dependencies  
RUN apt-get --no-install-recommends -y install \  
build-essential \  
autoconf \  
autotools-dev \  
automake \  
autogen \  
libtool \  
pkg-config \  
cmake \  
csh \  
gcc \  
gfortran \  
wget \  
git \  
pgplot5 \  
libfftw3-3 \  
libfftw3-bin \  
libfftw3-dev \  
libfftw3-single3 \  
libx11-dev \  
libltdl-dev \  
gsl-bin \  
libgsl-dev \  
libgsl2 \  
docker.io \  
openssh-server \  
xorg \  
openbox \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get -y clean  
  
# PGPLOT  
ENV PGPLOT_DIR /usr/lib/pgplot5  
ENV PGPLOT_FONT /usr/lib/pgplot5/grfont.dat  
ENV PGPLOT_INCLUDES /usr/include  
ENV PGPLOT_BACKGROUND white  
ENV PGPLOT_FOREGROUND black  
ENV PGPLOT_DEV /xs  
  
COPY sshd_config /etc/ssh/sshd_config  
USER psr  
  
# Define home, psrhome, OSTYPE and create the directory  
ENV HOME /home/psr  
ENV PSRHOME $HOME/software  
ENV OSTYPE linux  
RUN mkdir -p $PSRHOME  
WORKDIR $PSRHOME  
  
# Pull all repos  
RUN wget
http://www.atnf.csiro.au/people/pulsar/psrcat/downloads/psrcat_pkg.tar.gz && \  
tar -xvf psrcat_pkg.tar.gz -C $PSRHOME && \  
wget
http://www.imcce.fr/fr/presentation/equipes/ASD/inpop/calceph/calceph-2.3.0.tar.gz
&& \  
tar -xvvf calceph-2.3.0.tar.gz -C $PSRHOME && \  
git clone https://bitbucket.org/psrsoft/tempo2.git  
  
# calceph  
ENV CALCEPH $PSRHOME/calceph-2.3.0  
ENV PATH $PATH:$CALCEPH/install/bin  
ENV LD_LIBRARY_PATH $CALCEPH/install/lib  
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$CALCEPH/install/include  
WORKDIR $CALCEPH  
RUN ./configure --prefix=$CALCEPH/install --with-pic --enable-shared --enable-
static --enable-fortran --enable-thread && \  
make && \  
make check && \  
make install && \  
rm -f ../calceph-2.3.0.tar.gz  
  
# Psrcat  
ENV PSRCAT_FILE $PSRHOME/psrcat_tar/psrcat.db  
ENV PATH $PATH:$PSRHOME/psrcat_tar  
WORKDIR $PSRHOME/psrcat_tar  
RUN /bin/bash makeit && \  
rm -f ../psrcat_pkg.tar.gz  
  
# tempo2  
ENV TEMPO2 $PSRHOME/tempo2/T2runtime  
ENV PATH $PATH:$PSRHOME/tempo2/T2runtime/bin  
ENV C_INCLUDE_PATH $C_INCLUDE_PATH:$PSRHOME/tempo2/T2runtime/include  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$PSRHOME/tempo2/T2runtime/lib  
WORKDIR $PSRHOME/tempo2  
RUN sync && perl -pi -e 's/chmod \\+x/#chmod +x/' bootstrap # Get rid of:
returned a non-zero code: 126.  
RUN ./bootstrap && \  
./configure --x-libraries=/usr/lib/x86_64-linux-gnu --with-
calceph=$CALCEPH/install/lib --enable-shared --enable-static --with-pic
F77=gfortran CPPFLAGS="-I"$CALCEPH"/install/include" && \  
make -j $(nproc) && \  
make install && \  
make plugins-install && \  
rm -rf .git  
WORKDIR $PSRHOME/tempo2/T2runtime/observatory  
RUN mv observatories.dat observatories.dat_ORIGINAL && \  
mv aliases aliases_ORIGINAL && \  
wget
https://raw.githubusercontent.com/mserylak/pulsar_docker/master/tempo2/observatories.dat
&& \  
wget
https://raw.githubusercontent.com/mserylak/pulsar_docker/master/tempo2/aliases  
  
RUN env | awk '{print "export ",$0}' >> $HOME/.profile  
WORKDIR $HOME  
USER root  

