# calin/Dockerfile -- Stephen Fegan -- 2016-09-08  
#  
# Copyright 2016, Stephen Fegan <sfegan@llr.in2p3.fr>  
# LLR, Ecole Polytechnique, CNRS/IN2P3  
#  
# This file is part of "calin"  
#  
# "calin" is free software: you can redistribute it and/or modify it under the  
# terms of the GNU General Public License version 2 or later, as published by  
# the Free Software Foundation.  
#  
# "calin" is distributed in the hope that it will be useful, but WITHOUT ANY  
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR  
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.  
FROM llrcta/calin-docker-base:ubuntu16.04_v1.14  
  
MAINTAINER sfegan@llr.in2p3.fr  
  
#RUN apt-get update -y && apt-get install -y \  
# sqlite3 \  
# libsqlite3-dev  
  
ENV CC=gcc-5 CXX=g++-5  
  
ADD / /build/calin/  
  
RUN cd /build/calin && \  
mkdir mybuild && \  
cd mybuild && \  
cmake -DCALIN_BUILD_ARCH=generic \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=/usr \  
-DCALIN_PYTHON_SUB_DIR=lib/python3.5 \  
.. && \  
make -j2 && \  
make install && \  
cd / && \  
rm -rf /build  
  
CMD ["/usr/local/bin/jupyter-notebook"]  

