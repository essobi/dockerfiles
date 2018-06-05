FROM quay.io/loryza/mpi-fenics:latest  
MAINTAINER loryza <loryza@gmail.com>  
  
ENV PATH $FENICS_HOME/bin:$PATH  
ENV SRC_DIR /tmp/src  
  
RUN mkdir -p $SRC_DIR  
  
RUN apt-get install -y libhdf5-mpich-dev  
  
COPY bin $FENICS_HOME/bin  
COPY dolfin-adjoint.conf $FENICS_HOME/dolfin-adjoint.conf  
COPY fenics.env.conf $FENICS_HOME/fenics.env.conf  
  
RUN /bin/bash -c "fenics-pull && fenics-build"  
  
RUN /bin/bash -c "source $FENICS_HOME/dolfin-adjoint.conf && \  
pull_dolfin-adjoint && \  
build_dolfin-adjoint && \  
pull_libadjoint && \  
build_libadjoint"  
  
RUN cd $FENICS_HOME && mkdir src && cd src && git clone
https://github.com/jbornschein/mpi4py-examples.git  

