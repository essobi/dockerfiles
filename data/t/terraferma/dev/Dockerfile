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
# Builds a Docker image with a full installation of TerraFERMA.  
# The built image can be found at:  
#  
# https://hub.docker.com/r/terraferma/dev  
#  
# build using the TerraFERMA development environment  
FROM terraferma/dev-env:v0.9  
MAINTAINER terraferma <terraferma@lists.columbia.edu>  
  
USER root  
WORKDIR /tmp  
  
# install terraferma  
ENV TF_PREFIX /usr/local/terraferma  
RUN export PYTHONPATH=$FENICS_PREFIX/lib/python2.7/site-packages && \  
export PETSC_DIR=$PETSC_PREFIX && \  
export PATH=$FENICS_PREFIX/bin:$PATH && \  
export LD_LIBRARY_PATH=$FENICS_PREFIX/lib:$LD_LIBRARY_PATH && \  
export PKG_CONFIG_PATH=$FENICS_PREFIX/lib/pkgconfig:$PKG_CONFIG_PATH && \  
git clone -b v0.9 -q https://github.com/TerraFERMA/TerraFERMA.git && \  
cd TerraFERMA && \  
mkdir build && \  
cd build && \  
cmake -DCMAKE_INSTALL_PREFIX=${TF_PREFIX} \  
../. && \  
make && \  
make install && \  
rm -rf /tmp/* && \  
chgrp adm -R $TF_PREFIX && \  
chmod g+w -R $TF_PREFIX  
  
# install an environment module for terraferma  
COPY terraferma.configmodule /usr/local/share/environment-modules/terraferma  
  
WORKDIR $TF_HOME  
  
# link the installed tests and tutorials directories to the home directory  
USER tfuser  
COPY bash.load-modules $TF_HOME/.bash.load-modules  
RUN ln -s $TF_PREFIX/share/terraferma/tests $TF_HOME/tests && \  
ln -s $TF_PREFIX/share/terraferma/tutorials $TF_HOME/tutorials && \  
cat $TF_HOME/.bash.load-modules >> $TF_HOME/.profile  
COPY WELCOME $TF_HOME/WELCOME  
  
USER root  
  
  

