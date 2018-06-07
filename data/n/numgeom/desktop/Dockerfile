# Builds a Docker image for NumGeom development environment  
# with Ubuntu 16.04, Octave, Python3, Jupyter Notebook and Atom  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
  
FROM fastsolve/desktop:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
ARG SSHKEY_ID=secure  
ADD image/home $DOCKER_HOME/  
RUN chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
USER $DOCKER_USER  
  
###############################################################  
# Build NumGeom for Octave  
###############################################################  
RUN rm -f $DOCKER_HOME/.octaverc && \  
gd-get-pub -o - $(sh -c "echo '$SSHKEY_ID'") | tar xf - -C $DOCKER_HOME && \  
ssh-keyscan -H bitbucket.org >> $DOCKER_HOME/.ssh/known_hosts && \  
$DOCKER_HOME/bin/pull_numgeom && \  
$DOCKER_HOME/bin/pull_numgeom2 && \  
$DOCKER_HOME/bin/build_numgeom && \  
$DOCKER_HOME/bin/build_numgeom2 && \  
\  
rm -f $DOCKER_HOME/.ssh/id_rsa*  
  
  
WORKDIR $DOCKER_HOME/numgeom  
USER root  

