FROM ubuntu  
  
# Get required packages  
RUN apt-get update -y && \  
apt-get install -y gfortran \  
openmpi-bin \  
libopenmpi-dev \  
netcdf-bin \  
libnetcdf-dev \  
libhdf5-dev \  
libproj-dev \  
make \  
git \  
wget  
  
# Install Anaconda  
RUN wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh  
RUN /bin/bash Miniconda-latest-Linux-x86_64.sh -b -p /opt/conda  
ENV PATH /opt/conda/bin:$PATH  
RUN conda install -y numpy netCDF4  
  
# Install ParMetis-3.1Sept  
RUN git clone https://bitbucket.org/cmop-dev/parmetis-3.1-sep2010.git
/home/parmetis && cd /home/parmetis && make  
  
# Clone the test files into the docker container  
RUN git clone https://bitbucket.org/cmop-dev/selfe_fast_test.git
/home/selfe_fast_test  
  
# Use this script (name changes using pre-commit script) to update repo  
RUN cd /home/selfe_fast_test && echo FILE=$(ls update_*) > /etc/environment  
RUN . /etc/environment && bash /home/selfe_fast_test/$FILE # update_aa986cc.sh  

