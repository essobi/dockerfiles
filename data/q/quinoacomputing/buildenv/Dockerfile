FROM ubuntu:16.10  
RUN apt-get -q update -y  
RUN apt-get -qq install -y cmake gfortran gcc g++ openmpi-bin libopenmpi-dev
gmsh pegtl-dev libpugixml-dev libpstreams-dev libboost-all-dev liblapack-dev
liblapacke-dev libhdf5-dev libhdf5-openmpi-dev libhypre-dev wget trilinos-all-
dev libexodusii-dev python-pip git cmake libnetcdf-dev m4  
RUN wget -O /usr/bin/doxy-coverage
https://raw.githubusercontent.com/alobbs/doxy-coverage/master/doxy-coverage.py  
RUN chmod +x /usr/bin/doxy-coverage  
  
RUN groupadd -r quinoa  
RUN useradd -r -m -g quinoa quinoa  
USER quinoa  
ENV PATH=/usr/lib/ccache:${PATH}${PATH:+:}  
WORKDIR /home/quinoa  
RUN pip install --user codecov  

