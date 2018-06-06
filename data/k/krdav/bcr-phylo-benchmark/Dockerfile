### Using conda dockerfile template from:  
# https://fmgdata.kinja.com/using-docker-with-conda-environments-1790901398  
# Start from miniconda image:  
FROM continuumio/miniconda  
  
  
# Set the ENTRYPOINT to use bash  
# (this is also where you’d set SHELL,  
# if your version of docker supports this)  
ENTRYPOINT ["/bin/bash", "-c"]  
  
EXPOSE 5000  
# Install some essential things:  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
libpq-dev \  
build-essential \  
xvfb \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
# Some things to get perl PDL library installed:  
RUN apt-get update && apt-get install -y libblas-dev liblapack-dev gfortran  
  
# Install perl modules:  
RUN cpan PDL  
RUN cpan install PDL::LinearAlgebra::Trans  
  
# Use the conda environment yaml file to create the "bpb" conda environment:  
ADD environment_bpb.yml /tmp/environment_bpb.yml  
WORKDIR /tmp  
RUN ["conda", "env", "create", "-f", "environment_bpb.yml"]  
  
# Copy over the repository:  
WORKDIR /bcr-phylo-benchmark  
COPY . /bcr-phylo-benchmark  
  
# Tools to compile IgPhyML:  
RUN apt-get install -y autotools-dev automake  
  
# Compile IgPhyML (required to update hard-coded paths...):  
RUN cd tools/IgPhyML && ./make_phyml_omp && cd ../..  
  
# Run small test (this may take an hour and can be turned off).  
# Notice that we have to load the conda environment in the same process as the
test script  
# to execute the test under the "bpb" environment.  
RUN ["/bin/bash", "-c", "source activate bpb && ./test.sh"]  
  

