  
FROM jupyter/scipy-notebook:4.0  
# File Author / Maintainer  
MAINTAINER Nick Fyson  
  
# Update the repository sources list  
RUN apt-get -y update  
  
RUN apt-get -y install wget  
RUN apt-get -y install libxml2  
RUN apt-get -y install libxml2-dev  
RUN apt-get -y install zlib1g zlib1g-dev  
RUN apt-get -y install bzip2 libbz2-dev  
  
# install libsbml into python2 CONDA environment  
# early to avoid caching issues!  
RUN ($CONDA_DIR/envs/python2/bin/pip install python-libsbml)  
  
# install gurobi library  
RUN wget -q -O - http://packages.gurobi.com/gurobi-apt.sh | sudo sh  
  
# install additional library found necessary for running plotting  
RUN apt-get -y install libxrender1  
  
# install Pyabolism into python2 CONDA version  
# we install as under development, so if we map the relevant folder to the
source  
# on the host computer, changes will be reflected without restarting python  
WORKDIR /home/jovyan  
RUN git clone https://github.com/nickfyson/pyabolism.git  
WORKDIR /home/jovyan/pyabolism  
RUN $CONDA_DIR/envs/python2/bin/python setup.py develop  
  
# install python bindings into python2 CONDA version  
RUN (cd /opt/gurobi*/linux64 && $CONDA_DIR/envs/python2/bin/python setup.py
install)  
  
# copy examples directory  
RUN cp -R /home/jovyan/pyabolism/examples /home/jovyan/work  
RUN chown -R $NB_USER:users /home/$NB_USER/work/examples  
  
# add gurobi license files, if present  
# copies dummy file, to avoid failing when no license file is present  
COPY *.lic /home/$NB_USER/  
  
RUN (wget -q -O - https://bootstrap.pypa.io/ez_setup.py | python)  
RUN (pip install pip --upgrade)  
  
RUN (pip uninstall -y notebook)  
RUN (pip install notebook==4.1.0 --upgrade)  
  
# set the default working directory  
WORKDIR /home/jovyan  

