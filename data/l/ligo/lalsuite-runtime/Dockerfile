FROM ligo/base:stretch  
  
LABEL name="LALSuite Runtime - Debian Stretch" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20180430" \  
support="Reference Platform"  
# FIXME: openmpi-bin and openssh-client should be captured in lalsuite  
# dependencies  
RUN apt-get update && \  
apt-get \--assume-yes install \  
build-essential \  
python-glue \  
lscsoft-lalsuite \  
openmpi-bin \  
openssh-client && \  
apt-get \--assume-yes remove lal && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

