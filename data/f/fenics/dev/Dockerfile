# Builds a Docker image with the necessary libraries for compiling  
# FEniCS with Python 3. The image is publicly available at:  
#  
# https://hub.docker.com/r/fenics/dev  
#  
# Authors:  
# Lizao Li <lzlarryli@gmail.com>  
# Jack S. Hale <jack.hale@uni.lu>  
# Xiangmin Jiao <xiangmin.jiao@stonybrook.edu>  
# This Dockerfile is based on FEniCS dev Dockerfile at  
# https://bitbucket.org/fenics-project/docker/src/master/dockerfiles/dev/  
FROM fenics/dev-env:py3  
LABEL maintainer "Xiangmin Jiao <xiangmin.jiao@stonybrook.edu>"  
  
USER $DOCKER_USER  
  
ARG FENICS_BUILD_TYPE  
ENV FENICS_BUILD_TYPE ${FENICS_BUILD_TYPE:-Release}  
  
ARG FENICS_PYTHON  
ENV FENICS_PYTHON ${FENICS_PYTHON:-python3}  
  
ENV FENICS_PREFIX=$DOCKER_HOME/local  
  
RUN PYTHON3_VERSION=$($FENICS_PYTHON -c 'import sys;
print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))') && \  
echo "export PYTHONPATH=:$DOCKER_HOME/local/lib/python$PYTHON3_VERSION/site-
packages" >> $DOCKER_HOME/.profile && \  
echo 'source ~/fenics.env.conf' >> $DOCKER_HOME/.profile && \  
/bin/bash -l -c "PIP_NO_CACHE_DIR=off fenics-update"  
  
COPY WELCOME $DOCKER_HOME/WELCOME  
  
USER root  

