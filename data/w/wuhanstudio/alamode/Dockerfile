FROM ubuntu  
MAINTAINER wuhanstudio  
  
# ---------------------------------------------------------------  
# Prerequisites  
# ---------------------------------------------------------------  
RUN apt-get update  
RUN apt-get install -y wget tar build-essential git vim libblas-dev liblapack-
dev liblapacke-dev libboost-all-dev libfftw3-dev libeigen3-dev  
RUN rm -rf /var/lib/apt/lists/*  
RUN cp /usr/include/eigen3/* /usr/include/ -r  
  
# ---------------------------------------------------------------  
# MPICH2  
# ---------------------------------------------------------------  
RUN mkdir -p /opt/mpich2  
WORKDIR /opt/mpich2  
RUN wget http://www.mpich.org/static/downloads/3.2.1/mpich-3.2.1.tar.gz  
RUN tar -xvf mpich-3.2.1.tar.gz  
WORKDIR /opt/mpich2/mpich-3.2.1  
RUN ./configure --disable-fortran  
RUN make && make install  
  
# ---------------------------------------------------------------  
# LAPACK  
# ---------------------------------------------------------------  
RUN mkdir -p /opt/lapack  
WORKDIR /opt/lapack  
RUN wget http://www.netlib.org/lapack/lapack-3.8.0.tar.gz  
RUN tar -xvf lapack-3.8.0.tar.gz  
WORKDIR /opt/lapack/lapack-3.8.0  
RUN cp make.inc.example make.inc  
RUN make blaslib lapacklib lapackelib  
RUN cp librefblas.a /usr/lib/  
  
# ---------------------------------------------------------------  
# Boost  
# ---------------------------------------------------------------  
#apt-get install libboost-all-dev  
# ---------------------------------------------------------------  
# FFTW3  
# ---------------------------------------------------------------  
#apt-get install libfftw3-dev  
# ---------------------------------------------------------------  
# Eigen3  
# ---------------------------------------------------------------  
# apt-get install libeigen3-dev  
# ---------------------------------------------------------------  
# ALAMODE  
# ---------------------------------------------------------------  
RUN git clone http://github.com/ttadano/alamode.git /opt/alamode  
  
# ALM  
WORKDIR /opt/alamode/alm  
COPY Makefile.ALM Makefile  
# CXX = g++  
# CXXFLAGS = -O2 -std=c++11  
# LDFLAGS = -llapacke -llapack -lrefblas -lgfortran -lblas  
# LAPACK= -L /opt/lapack/lapack-3.8.0  
#alm: ${OBJS}  
# ${CXXL} ${CXXFLAGS} -o $@ ${OBJS} ${LIBS} ${LDFLAGS}  
RUN make  
  
# ANPHON  
WORKDIR /opt/alamode/anphon  
COPY Makefile.ANPHON Makefile  
#CXXFLAGS = -O3 -fopenmp -std=c++11  
#LDfLAGS = -lfftw3 -llapacke -llapack -lrefblas  
# anphon: ${OBJS}  
# ${LINKER} ${CXXFLAGS} -o $@ ${OBJS} ${LIBS} $(LDFLAGS)  
RUN make  
  
# TOOLS  
WORKDIR /opt/alamode/tools  
COPY Makefile.TOOLS Makefile  
# CXX = g++  
# CXXFLAGS = -O2 -std=c++11  
RUN make  
  
RUN mkdir /opt/work_dir  
ENV PATH=$PATH:/opt/alamode/alm:/opt/alamode/anphon:/opt/alamode/tools  

