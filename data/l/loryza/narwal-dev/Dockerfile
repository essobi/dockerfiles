FROM quay.io/loryza/trilinos-env:latest  
  
# Install instant  
RUN cd /tmp && \  
git clone https://bitbucket.org/fenics-project/instant.git && \  
cd instant && \  
python setup.py install --prefix=/usr/local  
  
# Install fiat  
RUN cd /tmp && \  
git clone https://bitbucket.org/fenics-project/fiat.git && \  
cd fiat && \  
python setup.py install --prefix=/usr/local  
  
# Install ufl  
RUN cd /tmp && \  
git clone https://bitbucket.org/narwal/ufl.git && \  
cd ufl && \  
python setup.py install --prefix=/usr/local  
  
# Install ffc  
RUN cd /tmp && \  
git clone https://bitbucket.org/narwal/ffc.git && \  
cd ffc && \  
python setup.py install --prefix=/usr/local  
  
# Install dolfin  
RUN cd /tmp && \  
git clone -b narwal https://bitbucket.org/narwal/dolfin.git && \  
cd dolfin && \  
mkdir -p build && \  
cd build && \  
cmake .. && \  
make install  
  
# Install narwal  
RUN cd /tmp && \  
git clone https://bitbucket.org/narwal/narwal.git && \  
cd narwal && \  
mkdir -p build && \  
cd build && \  
cmake .. && \  
make install && \  
rm -rf /tmp/*  

