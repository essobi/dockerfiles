FROM qnib/slurmd  
MAINTAINER "Christian Kniep <christian@qnib.org>"  
# Install dependencies  
RUN yum install -y openmpi-devel libmlx4 qperf infiniband-diags  
# Application libs  
RUN yum install -y gsl libgomp  
# bc  
RUN yum install -y bc  
  
RUN echo "source /etc/profile" >> /etc/bashrc  
RUN echo "module load mpi" >> /etc/bashrc  
  
# Stress  
#RUN yum install -y stress  
# ADD source code  
ADD opt/qnib/src/hello_mpi.c /opt/qnib/src/  
  
ADD opt/qnib/jobscripts/ /opt/qnib/jobscripts/  
ADD opt/qnib/bin/gemm_block_mpi_50ms /opt/qnib/bin/  
ADD opt/qnib/bin/gemm_block_mpi_250ms /opt/qnib/bin/  
ADD opt/qnib/bin/gemm_block_mpi_500ms /opt/qnib/bin/  
ADD opt/qnib/bin/generate_work.sh /opt/qnib/bin/generate_work.sh  
  
RUN pip install clustershell  
RUN echo "su -l -c 'sbatch -N2 /opt/qnib/jobscripts/gemm.sh 16384 500' alice"
>> /root/.bash_history && \  
echo "su -l -c 'sbatch -N4 /opt/qnib/jobscripts/ping_pong.sh' bob" >>
/root/.bash_history && \  
echo "/opt/qnib/bin/generate_work.sh 10 3 compute5" >> /root/.bash_history  
ADD etc/sensu/conf.d/check_ib.json /etc/sensu/conf.d/  
ADD opt/qnib/sensu/bin/check_ib.py /opt/qnib/sensu/bin/check_ib.py  
ENV SENSU_CHECK_IB=false  

