# Start from Debian image  
FROM debian:latest  
  
# Install requirements for GROMACS benchmark  
RUN apt-get update && apt-get install -y \  
openssh-client \  
openmpi-bin \  
libopenmpi-dev \  
fftw3 \  
cmake \  
wget \  
curl \  
build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
# Compile and install GROMACS  
RUN cd /tmp && \  
wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-5.1.4.tar.gz && \  
tar xzf gromacs-5.1.4.tar.gz && \  
cd gromacs-5.1.4 && \  
mkdir build && \  
cd build && \  
cmake \  
-DCMAKE_INSTALL_PREFIX=/benchmarks/gromacs/ \  
-DBUILD_SHARED_LIBS=off \  
-DBUILD_TESTING=off \  
-DREGRESSIONTEST_DOWNLOAD=OFF \  
-DCMAKE_C_COMPILER=`which mpicc` \  
-DCMAKE_CXX_COMPILER=`which mpicxx` \  
-DGMX_BUILD_OWN_FFTW=on \  
-DGMX_SIMD=AVX_256 \  
-DGMX_DOUBLE=off \  
-DGMX_EXTERNAL_BLAS=off \  
-DGMX_EXTERNAL_LAPACK=off \  
-DGMX_FFT_LIBRARY=fftw3 \  
-DGMX_GPU=off \  
-DGMX_MPI=on \  
-DGMX_OPENMP=on \  
-DGMX_X11=off \  
.. && \  
make -j 4 && \  
make install  
  
# Download GROMACS test data  
RUN mkdir /benchmarks/gromacs-datas && \  
cd /tmp && \  
wget http://www.prace-ri.eu/UEABS/GROMACS/1.2/GROMACS_TestCaseA.tar.gz && \  
tar xzf GROMACS_TestCaseA.tar.gz && \  
cp ion_channel.tpr /benchmarks/gromacs-datas  
  
# Install requirements for R benchmark  
RUN apt-get update && apt-get install -y \  
r-base \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install packages used for R benchmark  
COPY install_scripts /tmp/install_scripts  
RUN R CMD BATCH /tmp/install_scripts/install_rpackages.R  
  
# Install requirements for Python benchmark suite  
RUN apt-get update && apt-get install -y \  
python3-pip \  
python3-yaml \  
moreutils \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install packages for Python benchmark suite  
RUN pip3 install -U \  
psutil \  
pytest \  
pygal \  
pygal.js \  
pytest-benchmark  
  
# Copy benchmark scripts  
COPY benchmarks/benchmarks.py /benchmarks  
COPY benchmarks/R_GFA.R /benchmarks  
  
# Set result folder  
RUN mkdir /results  
  
# chown /benchmarks and results for a new user with uid 1001  
RUN chown 1001:1001 /benchmarks /results  
  
# Create user benchmark with uid 1001 (MPI is risky to run as root)  
RUN adduser --home /benchmarks --uid 1001 --shell /bin/bash --disabled-
password --gecos '' benchmark  
  
# Set default user and run location  
USER benchmark  
WORKDIR /benchmarks  
  
# Sed default command to run  
CMD savename=$(hostname)-$(date "+%0d-%0m-%Y_%H-%M-%S") && \  
cd /results && \  
if [ ! -e parameters.yml ] ; then \  
wget https://raw.githubusercontent.com/AaltoScienceIT/docker-fgci-
benchmark/master/benchmarks/parameters.yml ; \  
fi && \  
if [ ! -e reference.json ] ; then \  
wget https://raw.githubusercontent.com/AaltoScienceIT/docker-fgci-
benchmark/master/benchmarks/reference.json ; \  
fi && \  
pytest /benchmarks/benchmarks.py --benchmark-storage=/results \  
\--benchmark-save=$savename \  
\--benchmark-histogram=/results/histograms/$savename \  
\--benchmark-compare=/results/reference.json  

