FROM openkbs/docker-hpc-base  
  
MAINTAINER DrSnowbird "drsnowbird@openkbs.org"  
  
## Somehow OSU_VERSION:-5.4.1 build has some missing files. back to 5.3.2  
##  
  
## ARG OSU_VERSION=${OSU_VERSION:-5.4.1}  
ARG OSU_VERSION=${OSU_VERSION:-5.3.2}  
  
ARG OSU_DIR=osu-micro-benchmarks-${OSU_VERSION}  
ARG OSU_TGZ=${OSU_DIR}.tar.gz  
ARG OSU_OPENMPI_BUILD_DIR=build.openmpi  
  
RUN wget http://mvapich.cse.ohio-state.edu/download/mvapich/${OSU_TGZ} && \  
tar xvf ${OSU_TGZ} && \  
rm -rf ${OSU_TGZ} && \  
cd ${OSU_DIR} && \  
mkdir ${OSU_OPENMPI_BUILD_DIR} && \  
cd ${OSU_OPENMPI_BUILD_DIR} && \  
../configure CC=mpicc --prefix=$(pwd) && \  
make && make install  
  
## (other reference for the above build flags):  
## https://ulhpc-
tutorials.readthedocs.io/en/latest/advanced/OSU_MicroBenchmarks/  
##  
## ../src/osu-micro-benchmarks-5.4/configure CC=mpiicc CXX=mpiicpc
CFLAGS=-I$(pwd)/../src/osu-micro-benchmarks-5.4/util --prefix=$(pwd)  
  
#RUN echo $HOME  
#### ----------------------------  
#### ----- Application Entry ----  
#### ----------------------------  
# dummy entrypoint.sh file is used below  
#  
COPY entrypoint.sh /entrypoint.sh  
  
#### ---- OSU Benchmark ----  
## ENV OSU_MPI_DIR=/osu-micro-benchmarks-5.3.2/build.openmpi/libexec/osu-
micro-benchmarks/mpi  
ENV OSU_MPI_DIR=/${OSU_DIR}/${OSU_OPENMPI_BUILD_DIR}/libexec/osu-micro-
benchmarks/mpi  
# collective/osu_allgather  
# collective/osu_allgatherv  
# collective/osu_allreduce  
# collective/osu_alltoall  
# collective/osu_alltoallv  
# collective/osu_barrier  
# collective/osu_bcast  
# collective/osu_gather  
# collective/osu_gatherv  
# collective/osu_iallgather  
# collective/osu_iallgatherv  
# collective/osu_ialltoall  
# collective/osu_ialltoallv  
# collective/osu_ialltoallw  
# collective/osu_ibarrier  
# collective/osu_ibcast  
# collective/osu_igather  
# collective/osu_igatherv  
# collective/osu_iscatter  
# collective/osu_iscatterv  
# collective/osu_reduce  
# collective/osu_reduce_scatter  
# collective/osu_scatter  
# collective/osu_scatterv  
# one-sided/osu_acc_latency  
# one-sided/osu_cas_latency  
# one-sided/osu_fop_latency  
# one-sided/osu_get_acc_latency  
# one-sided/osu_get_bw  
# one-sided/osu_get_latency  
# one-sided/osu_put_bibw  
# one-sided/osu_put_bw  
# one-sided/osu_put_latency  
# pt2pt/osu_bibw  
# pt2pt/osu_bw  
# pt2pt/osu_latency  
# pt2pt/osu_latency_mt  
# pt2pt/osu_mbw_mr  
# pt2pt/osu_multi_lat  
# startup/osu_hello  
# startup/osu_init  
  
####  
#### ---- Usage ----  
#### The command from host:  
WORKDIR ${OSU_MPI_DIR}  
####  
# /usr/local/bin/singularity run ${INPUT_PATH}/${SINGULARITY_IMAGE_NAME}
collective/osu_reduce_scatter 2  
#/usr/local/bin/singularity run ${INPUT_PATH}/${SINGULARITY_IMAGE_NAME}
collective/osu_reduce_scatter 2  
ENTRYPOINT ["/entrypoint.sh"]  
  

