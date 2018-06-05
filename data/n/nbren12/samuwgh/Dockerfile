FROM debian:latest  
  
RUN apt-get update && apt-get install -y \  
libnetcdff-dev libnetcdf-dev \  
build-essential gfortran \  
libmpich-dev csh \  
gdb  
  
ADD SRC /sam/SRC  
ADD SRC/domain.f90 /sam/SRC/domain.f90  
ADD UTIL /sam/UTIL  
ADD RUNDATA /sam/RUNDATA  
ADD docker/Makefile /sam/Makefile  
ADD docker/Build /sam/Build  
  
RUN make -C /sam/UTIL  
RUN cd /sam && exec ./Build  
  
ADD CaseName /sam/CaseName  
ADD DYNAMO /sam/DYNAMO  
ADD RUNDATA /sam/RUNDATA  
  
WORKDIR /sam  
CMD mpirun -np 4 /sam/SAM_ADV_MPDATA_SGS_TKE_RAD_CAM_MICRO_SAM1MOM  

