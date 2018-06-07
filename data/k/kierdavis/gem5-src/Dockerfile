FROM debian:stable  
  
# Install dependencies.  
RUN apt-get update -y  
RUN apt-get install -y gcc g++ libgoogle-perftools-dev m4 mercurial python
python-dev scons swig zlib1g-dev  
  
# Obtain source.  
RUN hg clone http://repo.gem5.org/gem5 /opt/gem5  
  
# Patch source to fix the weird "kernel too old" bug.  
RUN sed -i s/3.0.0/6.3.0/ /opt/gem5/src/arch/arm/linux/process.cc  
  

