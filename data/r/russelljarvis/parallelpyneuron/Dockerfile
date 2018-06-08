#author russell jarvis rjjarvis@asu.edu  
#NEURON Dockerfile  
#Set the base image to Ubuntu  
FROM scidash/scipy-notebook-plus  
  
#Get a whole lot of GNU core development tools  
#version control java development, maven  
#Libraries required for building MPI from source  
#Libraries required for building NEURON from source  
#Also DO this part as root.  
USER root  
  
RUN apt-get update && apt-get install -y wget bzip2 ca-certificates default-
jre default-jdk maven emacs  
RUN apt-get update; apt-get install -y automake libtool git vim \  
wget python3 libpython3-dev libncurses5-dev libreadline-dev libgsl0-dev
cython3 \  
python3-pip python3-numpy python3-scipy python3-matplotlib python3-mock \  
ipython3 python3-docutils python3-yaml \  
python3-venv python3-mpi4py python3-tables cmake ssh  
  
#The following code is adapted from:  
#https://github.com/ContinuumIO/docker-images/blob/master/anaconda/Dockerfile  
#Do the rest of the build as user:  
#This will create a more familiar environment to continue developing in.  
#with less of a need to chown and chmod everything done as root at dockerbuild
completion  
#RUN apt-get update \  
# && apt-get install -y sudo \  
# && rm -rf /var/lib/apt/lists/*  
#RUN echo "jovyan ALL=NOPASSWD: ALL" >> /etc/sudoers  
USER jovyan  
WORKDIR /home/jovyan  
RUN sudo chown -R jovyan /home/jovyan  
ENV HOME /home/jovyan  
#ENV PATH /opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH  
RUN sudo /opt/conda/bin/conda install scipy numpy matplotlib  
  
#Test matplotlib  
#RUN python -c "import matplotlib"  
#Install General MPI, such that mpi4py can later bind with it.  
WORKDIR /home/jovyan  
  
WORKDIR $HOME  
RUN \  
wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.4/nrn-7.4.tar.gz && \  
tar -xzf nrn-7.4.tar.gz && \  
rm nrn-7.4.tar.gz  
  
WORKDIR $HOME/nrn-7.4  
RUN whereis python3  
RUN which mpirun  
ENV PATH
/usr/bin/python3/python:/opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH  
#RUN ls -ltr configure  
RUN ./configure --prefix=`pwd` --with-paranrn --without-iv --with-
nrnpython=/usr/bin/python3  
RUN sudo make all && \  
make install  
ENV PATH $HOME/nrn-7.4/x86_64/bin:$PATH  
  
  
  
ENV HOME /home/docker  
ENV PATH $HOME/nrn-7.4/x86_64/bin:$PATH  
ENV PATH /opt/conda/bin:/opt/conda/bin/conda:/opt/conda/bin/python:$PATH  
  
  
  
USER jovyan  
  
  
  
  
WORKDIR $HOME/git  
#TODO change back to this repository, once pull request as accepted for
python3 compliant code  
#RUN sudo git clone https://github.com/NeuroML/jNeuroML  
RUN sudo git clone https://github.com/russelljjarvis/jNeuroML.git  
WORKDIR $HOME/git/jNeuroML  
RUN sudo python getNeuroML.py  
  
RUN sudo chown -R jovyan /home/jovyan  
WORKDIR /home/jovyan/nrn-7.4/src/parallel  
RUN mpiexec -np 4 nrniv -mpi test0.hoc  
RUN mpiexec -np 4 nrniv -mpi test1.hoc  
RUN mpiexec -np 4 nrniv -mpi test2.hoc  
RUN mpiexec -np 4 nrniv -mpi test3.hoc  
RUN mpiexec -np 4 nrniv -mpi test4.hoc  
RUN mpiexec -np 4 nrniv -mpi test5.hoc  
RUN mpiexec -np 4 nrniv -mpi test6.hoc  
RUN mpiexec -np 4 nrniv -mpi test7.hoc  
  
ADD ./test_fixed.py /home/docker/nrn-7.4/src/parallel/  
RUN mpiexec -np 4 nrniv -mpi -python test_fixed.py  
RUN sudo pip3 install zmq  
RUN sudo pip3 install packaging  
RUN sudo pip3 install --upgrade pip#notebook  
RUN sudo pip3 install notebook  
RUN sudo pip3 install ipyparallel  
RUN sudo ipcluster nbextension enable  
RUN sudo ipython profile create chase  
RUN ipcluster start -n 4 --engines=MPIEngineSetLauncher  
#RUN sudo ipcluster start --profile=chase --debug &  
RUN mpiexec -n 4 ipengine --mpi=mpi4py

