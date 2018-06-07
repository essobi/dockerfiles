# Builds a Docker image for FEniCS stable version with Python 3,  
# built from git sources. The image is at:  
#  
# https://hub.docker.com/r/fenics/stable  
#  
# Authors:  
# Jack S. Hale <jack.hale@uni.lu>  
# Xiangmin Jiao <xiangmin.jiao@stonybrook.edu>  
FROM fenics/dev-env:py3  
LABEL maintainer "Xiangmin Jiao <xiangmin.jiao@stonybrook.edu>"  
  
USER root  
  
ENV FENICS_BUILD_TYPE=Release \  
FENICS_VERSION=2016.2.0 \  
FENICS_PYTHON=python3  
  
# Install fenics as root user into /usr/local then remove the fenics-* scripts  
# the fenics.env.conf file and the unnecessary $DOCKER_HOME/local directory as  
# the user does not need them in the stable image!  
RUN FENICS_SRC_DIR=/tmp/src $DOCKER_HOME/bin/fenics-pull && \  
sed -i -e 's/dim \/ 2/dim \/\/ 2/' /tmp/src/ffc/ffc/tensor/tensorreordering.py
&& \  
FENICS_SRC_DIR=/tmp/src $DOCKER_HOME/bin/fenics-build && \  
ldconfig && \  
rm -rf /tmp/src && \  
cp -r /usr/local/share/dolfin/demo $DOCKER_HOME/demo && \  
rm -rf $DOCKER_HOME/bin $DOCKER_HOME/fenics.env.conf && \  
chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
USER $DOCKER_USER  
  
# Make sure we get something that basically works on this stable build. It  
# would be better to run unit tests, but at the moment even the quick tests  
# take too long to run.  
RUN mkdir -p /tmp/poisson_test && \  
cd /tmp/poisson_test && \  
$FENICS_PYTHON $DOCKER_HOME/demo/documented/poisson/python/demo_poisson.py &&
\  
instant-clean && \  
rm -r /tmp/poisson_test  
  
COPY WELCOME $DOCKER_HOME/WELCOME  
  
USER root  

