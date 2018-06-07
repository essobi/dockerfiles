# Build as jupyterhub/singleuser  
# Run with the DockerSpawner in JupyterHub  
FROM jupyterhub/singleuser:latest  
  
MAINTAINER Project IDAES <scholia@lbl.gov>  
  
EXPOSE 8888  
USER root  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install gfortran locales && \  
/usr/sbin/update-locale LANG=C.UTF-8 && \  
locale-gen C.UTF-8 && \  
apt-get -y install autoconf && \  
apt-get --fix-missing -y install libboost-all-dev && \  
apt-get --fix-missing -y install libboost-python-dev && \  
apt-get -y install libtool && \  
apt-get -y install less && \  
apt-get remove -y locales && \  
apt-get -y install curl && \  
apt-get -y install subversion && \  
apt-get -y install coinor-cbc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
# Adding scripts to do installs here:  
ADD bootstrap /usr/local/src/bootstrap  
  
WORKDIR /usr/local/src  
  
# Install couenne  
RUN ./bootstrap/install_couenne.sh | tee ./bootstrap/install_couenne.log 2>&1  
  
# Install Ipopt  
RUN ./bootstrap/install_ipopt.sh | tee ./bootstrap/install_ipopt.log 2>&1  
  
# Installing supporting tools: ADOL-C, pyadolc , casadi, wrapper library:  
RUN ./bootstrap/install_supporting_tools.sh | tee
./bootstrap/install_suporting_tools.log 2>&1  
  
USER jovyan  
WORKDIR /home/jovyan  
  
# Add a basic "smoke test" here later, but for now just show python version  
CMD bash -c 'source activate python2 && python -V'  

