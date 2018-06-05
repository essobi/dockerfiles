FROM debian:7.9  
MAINTAINER Eric Suchyta <eric.d.suchyta@gmail.com>  
  
  
# "installed" ADIOS components in this image -- but I haven't necessarily
rigorously tested them  
#  
# transform:  
# compression: zlib, bzip2, szlib  
#  
# transport:  
# staging: dataspaces  
# extra filetypes: HDF5  
#  
# utilities:  
# bp2hdf, bp2cdf, gpp.py, python module,  
  
  
ENV prefix /prefix  
RUN mv /bin/sh /bin/sh.orig && ln -s /bin/bash /bin/sh && \  
mkdir $prefix && mkdir /software && \  
  
  
# apt install  
apt-get update && apt-get install -y \  
gcc g++ python-dev libmpich2-dev libxml2 gfortran \  
make build-essential libtool m4 automake \  
bzip2 libbz2-dev zlib1g zlib1g-dev \  
git wget \  
vim screen && \  
echo 'startup_message off' > ~/.screenrc && \  
  
  
# pip installs  
cd /software && wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
&& rm get-pip.py && \  
pip install numpy && \  
  
# MXML  
cd /software && wget http://www.msweet.org/files/project3/mxml-2.7.tar.gz && \  
tar xvzf mxml-2.7.tar.gz && rm mxml-2.7.tar.gz && cd mxml-2.7 && \  
./configure \--prefix=$prefix && make && make install && cd ../ && rm -r
mxml-2.7 && \  
  
# szlib-compression  
cd /software && wget http://www.hdfgroup.org/ftp/lib-
external/szip/2.1/src/szip-2.1.tar.gz && \  
tar xvzf szip-2.1.tar.gz && rm szip-2.1.tar.gz && cd szip-2.1 && \  
./configure \--prefix=$prefix && make && make install && cd ../ && rm -r
szip-2.1 && \  
  
# Dataspaces  
cd /software && wget https://googledrive.com/host/0B4AAwvZlUdfeX3BmN3ZUcTFmb0U
-O dataspaces-1.6.0.tar.gz && \  
tar xvzf dataspaces-1.6.0.tar.gz && rm dataspaces-1.6.0.tar.gz && cd
dataspaces-1.6.0 && ./autogen.sh && \  
CC=mpicc FC=mpif90 CFLAGS="-g -std=gnu99 -fPIC" LIBS="-lm" ./configure
\--prefix=$prefix \--enable-dart-tcp && make && make install && \  
cd ../ && rm -r dataspaces-1.6.0 && \  
  
  
# HDF5  
cd /software && wget
http://www.hdfgroup.org/ftp/HDF5/current/src/hdf5-1.8.17.tar.gz && \  
tar xvzf hdf5-1.8.17.tar.gz && rm hdf5-1.8.17.tar.gz && \  
  
# Parallel  
export SDIR=phdf5-1.8.17 && export PREFIX=$prefix/phdf5 && export
CODE=hdf5-1.8.17 && export LD_LIBRARY_PATH=$prefix/lib && \  
cp -r $CODE $SDIR && cd $SDIR && \  
CC=mpicc FC=mpif90 ./configure \--with-zlib=/usr \--with-szlib=$prefix
\--enable-fortran \--enable-parallel \--with-pic \--prefix=$PREFIX && \  
make && make install && cd ../ && rm -r $SDIR && \  
  
# Serial  
export SDIR=shdf5-1.8.17 && export PREFIX=$prefix/shdf5 && mv $CODE $SDIR &&
cd $SDIR && \  
CC=gcc FC=f95 ./configure \--with-zlib=/usr \--with-szlib=$prefix \--enable-
fortran \--prefix=$PREFIX && \  
make && make install && cd ../ && rm -r $SDIR && \  
  
  
# NetCDF4  
cd /software && wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.0.tar.gz
&& \  
tar xvzf netcdf-4.4.0.tar.gz && rm netcdf-4.4.0.tar.gz && \  
  
# Parallel...this doesn't work.  
# --with-nc4par=$prefix/pnc4 for ADIOS build breaks the build,  
# while giving include/lib dirs doesn't break it but doesn't know about the
parallel NetCDF4 build  
export PREFIX=$prefix/pnc4 && export SDIR=pnetcdf-4.4.0 && export
H5DIR=$prefix/phdf5 && export LD_LIBRARY_PATH=${H5DIR}/lib && export
CODE=netcdf-4.4.0 && \  
cp -r $CODE $SDIR && cd $SDIR && \  
#CC=mpicc FC=mpif90 CPPFLAGS=-I${H5DIR}/include LDFLAGS=-L${H5DIR}/lib
./configure --enable-netcdf4 --with-pic --prefix=$PREFIX && \  
#make && make install && \  
cd ../ && rm -r $SDIR && \  
  
# Serial  
export PREFIX=$prefix/snc4 && export SDIR=snetcdf-4.4.0 && export
H5DIR=$prefix/shdf5 && export LD_LIBRARY_PATH=${H5DIR}/lib && export
CODE=netcdf-4.4.0 && \  
mv $CODE $SDIR && cd $SDIR && \  
CC=gcc FC=f95 CPPFLAGS=-I${H5DIR}/include LDFLAGS=-L${H5DIR}/lib ./configure
\--enable-netcdf4 \--prefix=$PREFIX && \  
make && make install && cd ../ && rm -r $SDIR && \  
  
  
#zfp  
cd /software && wget http://computation.llnl.gov/projects/floating-point-
compression/download/zfp-0.5.0.tar.gz && \  
tar xvzf zfp-0.5.0.tar.gz && rm zfp-0.5.0.tar.gz && cd zfp-0.5.0 && make && \  
  
  
# updated version of automake  
apt-get remove \--purge -y automake && \  
cd /software && wget http://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz && \  
tar xvzf automake-1.15.tar.gz && rm automake-1.15.tar.gz && cd automake-1.15
&& \  
./configure && make && make install && cd ../ && rm -r automake-1.15  
  
#ADIOS  
RUN cd /software && git clone https://github.com/ornladios/ADIOS.git && \  
cd ADIOS && git checkout -b zfp origin/zfp && ./autogen.sh && \  
CFLAGS="-fPIC" MPICC=mpicc MPICXX=mpicxx MPIFC=mpif90 CC=gcc CXX=g++
FC=gfortran ./configure \  
\--prefix=$prefix \  
\--with-mxml=$prefix \  
\--with-dataspaces-incdir=$prefix/include \--with-dataspaces-
libdir=$prefix/lib \  
\--with-phdf5-incdir=$prefix/phdf5/include \--with-
phdf5-libdir=$prefix/phdf5/lib \  
\--with-hdf5-incdir=$prefix/shdf5/include \--with-
hdf5-libdir=$prefix/shdf5/lib \  
\--with-netcdf-incdir=$prefix/snc4/include \--with-netcdf-
libdir=$prefix/snc4/lib \  
#--with-nc4par-incdir=$prefix/pnc4/include --with-nc4par-
libdir=$prefix/pnc4/lib --with-nc4par-libs="-lhdf5_hl -lhdf5 -ldl -lm -lz" &&
\  
#--with-nc4par=$prefix/pnc4 && \  
\--with-bzip2=/usr \--with-zlib=/usr \--with-szip=$prefix \  
\--with-zfp=/software/zfp-0.5.0 && \  
make && make install && export PATH="$prefix/bin:${PATH}" && \  
cd wrappers/numpy/ && make MPI=y python && python setup.py install && \  
cd ../../../ && cd /software/ADIOS/config && git update-index \--assume-
unchanged libtool.m4 ltmain.sh ltoptions.m4 ltsugar.m4 ltversion.m4
lt~obsolete.m4 && \  
echo "TEST4"  
#cp -r adios-1.9.0/examples/ adios-examples && rm -r adios-1.9.0  
#git clone https://github.com/pnorbert/adiosvm.git  
###python -m pip uninstall -y pip setuptools wheel && rm -r /root/.cache/pip/
&& \  
### apt-get --purge autoremove -y libblas-dev scons git make libatlas-base-dev
pkg-config libpng12-dev && apt-get -y clean && \  
### apt-get remove --purge -y libicu-dev g++ libboost1.49-dev python2.7-dev
libicu48 gcc-4.7 g++-4.4 libopenmpi-dev cpp-4.7 libc6-dev cpp-4.4
libopenmpi1.3 binutils libmagic1 linux-libc-dev manpages-dev libfftw3-dev
libboost-wave1.49.0 libboost-math1.49.0 libboost-mpi-python1.49.0 libboost-
test1.49.0 libboost-serialization1.49.0 libboost-program-options1.49.0 && \  
# Environment setup for the main software  
RUN echo "export ADIOS_DIR=\"$prefix\"" > ~/.bashrc && \  
echo 'export PATH="${ADIOS_DIR}/bin:${PATH}"' >> ~/.bashrc && \  
echo 'export ADIOS_INC="$(adios_config -c)"' >> ~/.bashrc && \  
echo 'export ADIOS_LIB="$(adios_config -l)"' >> ~/.bashrc && \  
echo 'export
LD_LIBRARY_PATH="${ADIOS_DIR}/lib:${ADIOS_DIR}/phdf5/lib:/software/zfp-0.5.0/lib"'
>> ~/.bashrc && \  
echo 'export C_INCLUDE_PATH="${ADIOS_DIR}/include:/software/zfp-0.5.0/inc"' >>
~/.bashrc && \  
echo 'if [ -f ~/.bashrc ]; then source ~/.bashrc; fi' >> ~/.bash_profile && \  
echo 'export SCREEN_LD_LIBRARY_PATH="$LD_LIBRARY_PATH"' >> ~/.bashrc && \  
echo 'export LD_LIBRARY_PATH=$SCREEN_LD_LIBRARY_PATH' >> ~/.screenrc-ld && \  
echo -e '\nfunction zfp_config { if [ "$1" = "-c" ]; then echo
"-I/software/zfp-0.5.0/inc"; elif [ "$1" = "-l" ]; then echo
"-L/software/zfp-0.5.0/lib/ -lzfp -lm"; fi; }' >> ~/.bashrc && \  
echo 'function zfp_test { if [ "$1" != "--no-build" ]; then cd
/software/ADIOS/; make clean > makelog.txt && make >> makelog.txt && make
install >> makelog.txt; fi && cd /software/AtoZ/examples/ && mpicc -o write
write-simple.c $(adios_config -c) $(adios_config -l) && ./write && mpicc -o
read read-simple.c $(adios_config -c) $(adios_config -l) && ./read; cd
/software/ADIOS/; }' >> ~/.bashrc  
# This is to make interacting in the container more like how I want it.  
RUN apt-get install -y procps curl && \  
cd /software && git clone https://github.com/suchyta1/suchyta_utils.git && cd
suchyta_utils && python setup.py install && \  
  
mkdir -p ~/.vim/autoload ~/.vim/bundle && curl -LSso
~/.vim/autoload/pathogen.vim https://tpo.pe/pathogen.vim && mkdir ~/.vim/tmp
&& \  
git clone https://github.com/honza/dockerfile.vim.git
~/.vim/bundle/dockerfile.vim && \  
git clone https://github.com/klen/python-mode.git ~/.vim/bundle/python-mode &&
\  
git clone https://github.com/vim-airline/vim-airline.git ~/.vim/bundle/vim-
airline && \  
  
cd /software && \  
git clone https://github.com/suchyta1/configs.git && \  
ln -s /software/configs/vim ~/.vimrc && \  
ln -s /software/configs/git ~/.gitconfig && \  
mkdir ~/.ssh && ln -s /software/configs/ssh ~/.ssh/config && \  
cd ~ && wget
https://raw.githubusercontent.com/git/git/master/contrib/completion/git-
completion.bash && echo -e '\nsource ~/git-completion.bash' >> ~/.bashrc && \  
  
cd /software && git clone https://github.com/suchyta1/AtoZ.git  
#cd /software && mkdir adios-zfp && cd adios-zfp && git clone
https://github.com/ornladios/ADIOS.git && cd ADIOS && git checkout -b zfp
origin/zfp && \  

