FROM qnib/cluster  
  
# Install dependencies  
RUN yum install -y openmpi libmlx4 infiniband-diags gsl bc  
RUN echo "source /etc/profile" >> /etc/bashrc  
RUN echo "module load mpi" >> /etc/bashrc  
  
RUN yum install -y iperf qperf  
RUN yum install -y gcc-c++ libgomp openmpi-devel make  
## HPCG  
RUN curl -sfL http://www.hpcg-benchmark.org/downloads/hpcg-3.0.tar.gz | tar
xzf - -C /opt/ && \  
mkdir /opt/hpcg-3.0/Linux_MPI && \  
cd /opt/hpcg-3.0/Linux_MPI && \  
/opt/hpcg-3.0/configure Linux_MPI && \  
source /etc/profile && \  
module load mpi && \  
make -j2  
RUN curl -sfL https://www.nersc.gov/assets/Trinity--
NERSC-8-RFP/Benchmarks/July12/osu-micro-benchmarks-3.8-July12.tar | tar xf -
-C /opt/  
RUN cd /opt/osu-micro-benchmarks-3.8-July12/ && \  
source /etc/profile && \  
module load mpi && \  
./configure && make && make install  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_acc_latency  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_get_bw  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_get_latency  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_passive_acc_latency  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_passive_get_bw  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_passive_get_latency  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_passive_put_bw  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_passive_put_latency  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_put_bibw  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_put_bw  
#/usr/local/libexec/osu-micro-benchmarks/mpi/one-sided/osu_put_latency  

