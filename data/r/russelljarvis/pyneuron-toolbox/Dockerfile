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
emacs vim \  
default-jre default-jdk maven xterm  
  
#The following code is adapted from:  
#https://github.com/ContinuumIO/docker-images/blob/master/anaconda/Dockerfile  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-3.7.0-Linux-x86_64.sh -O
miniconda.sh -O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
  
#Do the rest of the build as user:  
#This will create a more familiar environment to continue developing in.  
#with less of a need to chown and chmod everything done as root at dockerbuild
completion  
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
RUN sudo /opt/conda/bin/conda install scipy numpy  
  
#Install General MPI, such that mpi4py can later bind with it.  
WORKDIR /home/docker  
  
RUN \  
sudo wget https://www.open-
mpi.org/software/ompi/v2.0/downloads/openmpi-2.0.0.tar.gz && \  
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
sudo wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.4/nrn-7.4.tar.gz
&& \  
sudo tar -xzf nrn-7.4.tar.gz && \  
sudo rm nrn-7.4.tar.gz  
  
WORKDIR /home/docker/neuron/nrn-7.4  
RUN sudo ./configure --prefix=`pwd` --without-iv --with-
nrnpython=/opt/conda/bin/python --with-paranrn=/usr/bin/mpiexec  
RUN sudo make all && \  
sudo make install  
  
#Create python bindings for NEURON  
WORKDIR src/nrnpython  
RUN sudo /opt/conda/bin/python setup.py install  
ENV PATH=$HOME/neuron/nrn-7.4/x86_64/bin:$PATH  
  
  
#Get JNeuroML  
RUN echo $PATH  
WORKDIR /home/docker/git  
#TODO change back to this repository, once pull request as accepted for
python3 compliant code  
#RUN git clone https://github.com/NeuroML/jNeuroML  
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
  
RUN /opt/conda/bin/python -c "import tempita"  
RUN sudo /opt/conda/bin/conda install -y libxml2 libxslt lxml  
RUN sudo apt-get install -y gcc  
  
#WORKDIR /home/docker/git  
#RUN sudo git clone https://github.com/takluyver/entrypoints.git  
#WORKDIR /home/docker/git/takluyver  
#The following code is adapted from:  
#https://github.com/dmaticzka/docker-edenbase  
#https://github.com/rgerkin/docker-edenbase  
RUN sudo /opt/conda/bin/conda install -y jupyter  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
#entrypoints: 0.2.2-py34_0  
#The non development versions of sciunit, neuronunit build  
#The dev branchs fail  
#Test by uncommenting the below:  
#CMD ls *  
#RUN python -c "import sys; print(sys.path)"  
#RUN sudo ln -s entrypoints/entrypoints.py /opt/conda/lib/python3.4/site-
packages  
RUN python -c "import entrypoints"  
#RUN sudo /opt/conda/bin/python setup.py install  
WORKDIR /home/docker/git  
RUN sudo git clone https://github.com/scidash/sciunit -b dev  
#sciunit  
WORKDIR /home/docker/git/sciunit  
RUN sudo /opt/conda/bin/python setup.py install  
  
WORKDIR /home/docker/git  
RUN sudo git clone https://github.com/scidash/neuronunit -b dev  
WORKDIR /home/docker/git/neuronunit  
RUN sudo /opt/conda/bin/python setup.py install  
  
#ADD requirements.txt .  
#The purpose is to create a notebook web server without having a web browser o
ra #graphical front end  
##from jupyter documentation  
#Add Tini. Tini operates as a process subreaper for jupyter. This prevents  
#kernel crashes.  
#ENV TINI_VERSION v0.6.0  
#ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
#RUN sudo chmod +x /usr/bin/tini  
#ENTRYPOINT ["/usr/bin/tini", "--"]  
#RUN sudo mkdir /export  
#EXPOSE 8888  
#CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "
--notebook-dir=/export/"]  
#RUN alias jup='jupyter notebook --port=8888 --no-browser --ip=0.0.0.0
--notebook-dir=/export/'  
RUN sudo chown -R docker $HOME  
WORKDIR /home/docker/  

