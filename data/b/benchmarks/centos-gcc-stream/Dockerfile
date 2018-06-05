FROM benchmarks/centos-gcc  
MAINTAINER Nico Mittenzwey <nico.mittenzwey+docker@gmail.com>  
# Prepare directory and get source code  
RUN mkdir /usr/src/stream/ && \  
cd /usr/src/stream/ && \  
curl -OSL https://www.cs.virginia.edu/stream/FTP/Code/stream.c  
  
# Get startup file  
RUN cd /root/ && \  
curl -OSL https://raw.githubusercontent.com/hpc-
training/docker/master/benchmarks/centos-gcc-stream/run-benchmark.sh && \  
chmod a+x ./run-benchmark.sh  
  
# Command to start when image is run  
CMD ["/root/run-benchmark.sh"]  

