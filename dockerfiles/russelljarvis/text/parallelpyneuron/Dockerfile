#author russell jarvis rjjarvis@asu.edu
#NEURON Dockerfile
#Set the base image to Ubuntu
FROM ubuntu
#Get a whole lot of GNU core development tools
#version control java development, maven
#Libraries required for building MPI from source
#Libraries required for building NEURON from source
#Also DO this part as root.
RUN apt-get update && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git gcc g++ build-essential \ 
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    libncurses-dev openmpi-bin openmpi-doc libopenmpi-dev \
    default-jre default-jdk maven emacs
    
#The following code is adapted from:
#https://github.com/ContinuumIO/docker-images/blob/master/anaconda/Dockerfile    
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O miniconda.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh

#Do the rest of the build  as user:
#This will create a more familiar environment to continue developing in.
#with less of a need to chown and chmod everything done as root at dockerbuild completion
RUN useradd -ms /bin/bash docker
USER root
RUN apt-get update \
      && apt-get install -y sudo \
      && rm -rf /var/lib/apt/lists/*
RUN echo "docker ALL=NOPASSWD: ALL" >> /etc/sudoers

USER docker
WORKDIR /home/docker
RUN chown -R docker:docker /home/docker
ENV HOME /home/docker 
ENV PATH /opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH
RUN sudo /opt/conda/bin/conda install scipy numpy matplotlib

#Test matplotlib
RUN /opt/conda/bin/python -c "import matplotlib"
#Install General MPI, such that mpi4py can later bind with it.
WORKDIR /home/docker

RUN \
   sudo wget https://www.open-mpi.org/software/ompi/v2.0/downloads/openmpi-2.0.0.tar.gz && \
   sudo tar -xzf openmpi-2.0.0.tar.gz && \
   sudo rm openmpi-2.0.0.tar.gz

WORKDIR /home/docker/openmpi-2.0.0

# Compile openmpi
RUN \
  sudo ./configure && \
  sudo make all && \
  sudo make install

# Get python bindings for open mpi
WORKDIR $HOME
RUN sudo /opt/conda/bin/conda install -y mpi4py ipython

#Install NEURON-7.4 with python, with MPI. An infamous build process,
#and much of the motivation for this docker container
WORKDIR /home/docker/neuron
# Fetch NEURON source files, extract them, delete .tar.gz file.
RUN \
  sudo wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.4/nrn-7.4.tar.gz && \
  sudo tar -xzf nrn-7.4.tar.gz && \
  sudo rm nrn-7.4.tar.gz 

WORKDIR /home/docker/neuron/nrn-7.4
RUN sudo ./configure --prefix=`pwd` --without-iv --with-nrnpython=/opt/conda/bin/python --with-paranrn=/usr/bin/mpiexec
RUN sudo make all && \
   sudo make install

#Create python bindings for NEURON
WORKDIR src/nrnpython
RUN sudo /opt/conda/bin/python setup.py install
ENV PATH $HOME/neuron/nrn-7.4/x86_64/bin:$PATH


#Get JNeuroML
RUN echo $PATH
WORKDIR /home/docker/git
#TODO change back to this repository, once pull request as accepted for python3 compliant code
#RUN sudo git clone https://github.com/NeuroML/jNeuroML
RUN sudo git clone https://github.com/russelljjarvis/jNeuroML.git
WORKDIR jNeuroML
RUN sudo /opt/conda/bin/python getNeuroML.py

#Begin installation of neuronunit.
WORKDIR /home/docker/git
RUN sudo git clone https://github.com/rgerkin/rickpy
WORKDIR /home/docker/git/rickpy
RUN sudo /opt/conda/bin/python setup.py install

WORKDIR $HOME
RUN sudo /opt/conda/bin/conda install -y tempita cython

RUN sudo /opt/conda/bin/conda install -y libxml2 libxslt lxml
RUN sudo apt-get install -y gcc

RUN sudo /opt/conda/bin/conda install -y jupyter

#sciunit
WORKDIR /home/docker/git
RUN sudo git clone https://github.com/scidash/sciunit -b dev
WORKDIR /home/docker/git/sciunit
RUN sudo /opt/conda/bin/python setup.py install

#neuronunit
WORKDIR /home/docker/git
RUN sudo git clone https://github.com/scidash/neuronunit -b dev
WORKDIR /home/docker/git/neuronunit
RUN sudo /opt/conda/bin/python setup.py install

#TODO create a notebook web server without having a web browser or a graphical front end
#In the future code to do this will be based on:
#https://github.com/dmaticzka/docker-edenbase
#https://github.com/rgerkin/docker-edenbase
#Unsure if getting pip is still necessary.
RUN sudo apt-get update && sudo apt-get install -y python3-setuptools
RUN sudo apt-get install -y pandoc
RUN sudo easy_install3 pip

ENV HOME /home/docker 
ENV PATH /opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH

ENV PATH $HOME/neuron/nrn-7.4/x86_64/bin:$PATH

RUN sudo chown -R docker $HOME

WORKDIR /home/docker/git
RUN git clone https://github.com/soravux/scoop.git
WORKDIR /home/docker/git/scoop
RUN sudo /opt/conda/bin/python setup.py install

WORKDIR /home/docker/git
RUN git clone https://github.com/DEAP/deap.git
WORKDIR /home/docker/git/deap
RUN sudo /opt/conda/bin/python setup.py install

#The volume command declares a volume of persistant memory for the docker container.
#This will be useful for ongoing development.
#VOLUME
# TODO uncomment and test:
#WORKDIR /home/docker/git
#RUN git https://github.com/OpenSourceBrain/Thalamocortical.git
#WORKDIR /home/docker/git/Thalamocortical/NeuroML2/pythonScripts/netbuild/
#RUN jNeuroML -neuron -netPyNN TestSmall.net.nml
#Some superficial tests to check for breaks.
RUN nrniv
RUN mpiexec -np 4 python -c "import mpi4py"
RUN python -c "import neuron; import sciunit; import neuronunit"
RUN nrnivmodl 
RUN echo "that last stderr may have looked bad, but it was probably an indication that nrnivmodl can work if given mod files"
RUN python -c "import scoop; import deap"

RUN sudo /opt/conda/bin/conda install matplotlib

    Contact GitHub API Training Shop Blog About 

    © 2016 GitHub, Inc. Terms Privacy Security Status Help 


