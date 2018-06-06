FROM quay.io/fenicsproject/dev-env:latest  
  
USER root  
  
# Install some additional packages on top of standard FEniCS dev-env  
RUN apt-get -qq update && \  
apt-get -y \--with-new-pkgs \  
-o Dpkg::Options::="--force-confold" upgrade && \  
apt-get -y install python3-lxml gmsh valgrind && \  
apt-get clean && \  
update-alternatives --set mpirun /usr/bin/mpirun.mpich && \  
update-alternatives --set mpi /usr/include/mpich && \  
python3 -m pip install --no-binary=h5py h5py && \  
python3 -m pip install PyYAML && \  
python3 -m pip install git+https://github.com/nschloe/meshio.git && \  
cd /tmp && \  
wget -nc --quiet http://gmsh.info/bin/Linux/gmsh-3.0.6-Linux64.tgz && \  
tar -xf gmsh-3.0.6-Linux64.tgz && \  
mv gmsh-3.0.6-Linux64/bin/* /usr/local/bin && \  
wget -nc --quiet https://github.com/pybind/pybind11/archive/v2.2.1.tar.gz && \  
tar -xf v2.2.1.tar.gz && \  
cd pybind11-2.2.1 && \  
mkdir build-dir && cd build-dir && \  
cmake -DPYBIND11_TEST=off -DCMAKE_INSTALL_PREFIX=/usr/local ../ && \  
make install && \  
cd && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

