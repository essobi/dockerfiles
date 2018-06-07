#  
# Debian Jessie container with MPICH 3.2 and the OSU benchmarks 5.3  
#  
FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y file \  
g++ \  
gcc \  
gfortran \  
libmpich-dev \  
make \  
mpich \  
\--no-install-recommends  
  
#  
# install the OSU Micro-Benchmarks from source  
#  
ENV CC gcc  
ENV CXX g++  
ENV F90 gfortran  
ENV MPIF90 mpif90  
ADD src/osu-micro-benchmarks-5.3.tar.gz /usr/local/src  
RUN cd /usr/local/src/osu-micro-benchmarks-5.3 && \  
./configure --prefix=/usr/local CC=$( which mpicc ) CXX=$( which mpicxx ) && \  
make && \  
make install  
  
# cleanup  
RUN rm -r /usr/local/src/osu-micro-benchmarks-5.3  
  
WORKDIR /usr/local/libexec/osu-micro-benchmarks/mpi/pt2pt  
  
CMD ["mpiexec", "-n", "2", "-bind-to", "core", "./osu_bw"]  

