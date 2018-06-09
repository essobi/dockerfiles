# Image: gzynda/tacc-stamped2-mpi  
# Version: 0.0.1  
  
# Based on Ubuntu 18.04 LTS  
FROM gzynda/tacc-base:latest  
  
########################################  
# Install mpich  
########################################  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends \  
vim-nox mpich libmpich-dev build-essential && \  
docker-clean  

