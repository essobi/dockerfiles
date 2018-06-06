# Copyright (C) 2013 Columbia University in the City of New York and others.  
#  
# Please see the AUTHORS file in the main source directory for a full list  
# of contributors.  
#  
# This file is part of TerraFERMA.  
#  
# TerraFERMA is free software: you can redistribute it and/or modify  
# it under the terms of the GNU Lesser General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# TerraFERMA is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU Lesser General Public License for more details.  
#  
# You should have received a copy of the GNU Lesser General Public License  
# along with TerraFERMA. If not, see <http://www.gnu.org/licenses/>.  
#  
#  
# Builds a Docker image with a full installation of TerraFERMA and the  
# tutorial materials for CIDER 2017, Berkeley, CA.  
# The built image can be found at:  
#  
# https://hub.docker.com/r/terraferma/cider_tutorials  
#  
# build using the TerraFERMA v1.0.1  
FROM terraferma/dev:v1.0.1  
MAINTAINER terraferma <terraferma@lists.columbia.edu>  
  
USER root  
WORKDIR /tmp  
  
# install a few extra packages  
RUN apt-get update && \  
apt-get -y --with-new-pkgs \  
-o Dpkg::Options::="--force-confold" -o Dpkg::Options::="--force-confdef" upgrade && \  
apt-get -y install \  
eog && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
USER tfuser  
WORKDIR $TF_HOME  
  
# set some useful aliases  
COPY bash_aliases $TF_HOME/.bash_aliases  
# update welcome message  
COPY WELCOME $TF_HOME/WELCOME  
  
# install and build the CIDER tutorials  
RUN export PYTHONPATH=$TF_PREFIX/lib/python2.7/site-
packages:$FENICS_PREFIX/lib/python2.7/site-packages && \  
export PATH=$TF_PREFIX/bin:$FENICS_PREFIX/bin:$PATH && \  
export LD_LIBRARY_PATH=$FENICS_PREFIX/lib:$LD_LIBRARY_PATH && \  
export PETSC_DIR=$PETSC_PREFIX && \  
export PKG_CONFIG_PATH=$FENICS_PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH && \  
export
DIAMOND_CONFIG_PATH=$TF_PREFIX/share/buckettools/diamond:$DIAMOND_CONFIG_PATH
&& \  
export
CMAKE_MODULE_PATH=$TF_PREFIX/share/buckettools/cmake/modules:$CMAKE_MODULE_PATH
&& \  
export TF_CMAKE_PATH=$TF_PREFIX/share/terraferma/cpp && \  
git clone -q https://github.com/TerraFERMA/cider_tutorials.git && \  
cd cider_tutorials && \  
tfsimulationharness --build *.shml  
  
USER root  
  

