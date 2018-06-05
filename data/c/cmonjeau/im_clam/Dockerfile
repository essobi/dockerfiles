################################################  
# Dockerfile to build im_clam software  
# Based on debian  
################################################  
  
FROM debian  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc git libglib2.0-dev cmake pkg-config gsl-bin
libnlopt-dev libsuitesparse-dev libgsl0-dev mpi-default-bin  
  
ENV PETSC_URL http://ftp.mcs.anl.gov/pub/petsc/release-
snapshots/petsc-3.5.4.tar.gz  
ENV PETSC_DIR /opt/petsc-3.5.4  
ENV PETSC_ARCH "arch-linux2-c-debug"  
  
  
ENV SLEPC_URL
http://slepc.upv.es/download/download.php?filename=slepc-3.5.4.tar.gz  
ENV SLEPC_DIR /opt/slepc-3.5.4  
  
ENV IM_CLAM_URL https://github.com/kern-lab/im_clam  
ENV IM_CLAM_PATH /opt/im_clam  
  
################## Update & upgrade ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## Install PETSC ######################  
  
WORKDIR /opt  
RUN wget ${PETSC_URL} -O - | tar xvzf -  
WORKDIR ${PETSC_DIR}  
RUN ./configure --download-f2cblaslapack --download-mpich  
RUN make PETSC_DIR=${PETSC_DIR} PETSC_ARCH=${PETSC_ARCH} all  
  
  
################## Install SLEPC ######################  
WORKDIR /opt  
RUN wget ${SLEPC_URL} -O - | tar xvzf -  
  
WORKDIR ${SLEPC_DIR}  
  
RUN ./configure  
RUN make  
RUN make test  
  
################# INSTALL IM_CLAM ######################  
RUN apt-get install -y  
  
WORKDIR /opt  
RUN git clone ${IM_CLAM_URL}  
WORKDIR ${IM_CLAM_PATH}  
RUN make all  
  
RUN cp im_clam /usr/local/bin/  
  
###############################################################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  

