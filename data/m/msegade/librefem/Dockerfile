FROM centos:7  
MAINTAINER miguelrsegade@gmail.com  
  
# Update and prerequisites  
RUN yum clean all && \  
yum -y update && \  
yum -y install wget bzip2 \  
gawk \  
make cmake \  
gdb \  
xterm \  
gcc gcc-c++ gcc-gfortran \  
python python-devel numpy python-qt4 \  
tk \  
bison flex \  
blas blas-devel lapack lapack-devel \  
zlib-devel \  
gnuplot \  
sudo && \  
yum clean all && \  
rm -rf /var/cache/*  
  
# Install Code_Aster  
ARG ASTER_ROOT=/opt/aster  
ARG ASTER_VERSION=13.4.0-1  
RUN mkdir $ASTER_ROOT  
  
#COPY ["aster-full-src-13.4.0-1.noarch.tar.gz", "/aster-full-
src-13.4.0-1.noarch.tar.gz"]  
RUN wget "http://www.code-aster.org/FICHIERS/aster-full-
src-$ASTER_VERSION.noarch.tar.gz"  
RUN tar xf "./aster-full-src-$ASTER_VERSION.noarch.tar.gz" && \  
pushd aster-full-src-* && \  
python setup.py install --prefix=$ASTER_ROOT \--noprompt --quiet hdf5 \  
med \  
gmsh \  
grace \  
gibi \  
scotch \  
astk \  
metis \  
mfront \  
mumps \  
homard && \  
echo "HOME_HOMARD = '/opt/aster'" >> setup.cfg && \  
python setup.py install --prefix=$ASTER_ROOT \--noprompt --quiet aster && \  
popd && \  
rm -rf ./aster-full-src-*  
  
# Default user without password and sudo  
ARG USER=librefem  
RUN adduser $USER  
RUN passwd -d $USER  
RUN usermod -aG wheel $USER  
  
# Set permissions and enviromental variables  
RUN chown -R $USER:$USER /home/$USER  
USER $USER  
ENV HOME /home/$USER  
ENV USER $USER  
ENV PATH "$PATH:/opt/aster/bin"  
WORKDIR $HOME  
  

