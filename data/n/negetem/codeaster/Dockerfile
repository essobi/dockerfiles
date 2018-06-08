# ----------------------  
# Docker's informations:  
# ----------------------  
FROM ubuntu:16.04  
MAINTAINER Jocelyn LOPEZ <jocelyn.lopez.pro@gmail.com>  
  
# ----------------  
# Set environment:  
# ----------------  
ARG ASTER_ROOT=/opt/aster  
ARG ASTER_VERSION=12.6.0-4  
COPY ["codeaster.sh", "/codeaster.sh"]  
  
# --------------------------  
# Install required packages:  
# --------------------------  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget \  
make \  
cmake \  
gdb \  
gawk \  
gcc \  
g++ \  
gfortran \  
python \  
python-dev \  
python-numpy \  
python-qt4 \  
tk \  
bison \  
flex \  
liblapack-dev \  
zlib1g-dev \  
gnuplot \  
ddd \  
nedit \  
grace \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN chmod +x /codeaster.sh  
RUN /codeaster.sh install $ASTER_VERSION $ASTER_ROOT  
  
# ----------------------------------------  
# Make available as_run outside container:  
# ----------------------------------------  
WORKDIR $ASTER_ROOT  
ENTRYPOINT ["bin/as_run"]  

