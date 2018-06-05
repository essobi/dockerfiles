FROM paternal/pythons:stretch  
LABEL maintainer "Louis Paternault <spalax+docker@gresille.org>"  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN echo 'deb http://httpredir.debian.org/debian jessie main' >
/etc/apt/sources.list.d/jessie.list  
RUN \  
apt-get --yes update && \  
apt-get install --yes --allow-remove-essential --target-release jessie \  
libpython3.4 \  
libpython3.4-dev \  
libpython3.4-minimal \  
libpython3.4-stdlib \  
python3.4 \  
python3.4-dev \  
python3.4-minimal \  
&& \  
apt-get clean  
  
# Print versions  
RUN for bin in python python2.7 python3 python3.4 python3.5 python3.6 pypy
jython tox; \  
do \  
echo "$bin $($bin --version 2>&1)"; \  
done  

