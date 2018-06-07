# Pull a unbunuu wiht a prebuild environment  
FROM fremling/hammer-environment:latest  
##FROM ubuntu:14.04  
MAINTAINER Niall Moran <niall.moran@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
##Clone into the hammer image  
RUN git clone https://bitbucket.org/nmoran/hammer.git  
  
WORKDIR /hammer/Hammer  
###Install some extra hammer requirements  
RUN cat requirements.txt | xargs pip install  
  
### FIXME The MPI-implementation fails with the pip-install, so adding the
ubuntu binaries as well....  
RUN apt-get install -y python-mpi4py  
RUN python setup_f2py.py install  
RUN python setup.py install  
RUN python setup.py test  
  
# now build CFT wave-function generator code  
WORKDIR /hammer/CFT_wave_functions  
RUN make notest  
RUN make  
  
# Build the documentation for building the documentation  
WORKDIR /hammer/docs  
RUN make html  
  
##Install the FQHE utilities for the sphere  
WORKDIR /hammer  
RUN git clone https://jfulse@bitbucket.org/jfulse/fqhe_mc_sphere.git  
WORKDIR /hammer/fqhe_mc_sphere  
RUN make  
  
###Return to Hammer root  
WORKDIR /hammer  

