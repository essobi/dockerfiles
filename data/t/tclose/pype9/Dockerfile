#  
# A Docker image for running PyPe9 examples  
#  
# Steps to run the examples using Docker:  
#  
# 1. Install Docker (see https://docs.docker.com/engine/installation/)  
#  
# 2. Pull the Pype9 "Docker image"  
#  
# docker pull tclose/pype9  
#  
# 3. Create a "Docker container" from the downloaded image  
#  
# docker run -v `pwd`/<your-local-output-dir>:/home/docker/output -t -i
tclose/pype9 /bin/bash  
#  
# This will create a folder called <your-local-output-dir> in the  
# directory you are running the docker container, which you can access  
# from your host computer (i.e. outside of the container) and view the  
# output figures from.  
#  
# 4. From inside the running container, you will be able to run pype9, e.g.  
#  
# pype9 simulate \  
# ~/catalog/neuron/HodgkinHuxley#PyNNHodgkinHuxleyProperties \  
# nest 500.0 0.001 \  
# --init_value v 65 mV \  
# --init_value m 0.0 unitless \  
# --init_value h 1.0 unitless \  
# --init_value n 0.0 unitless \  
# --record v ~/output/hh-v.neo.pkl  
#  
# pype9 plot ~/output/hh-v.neo.pkl --save ~/output/hh-v.png  
#  
# Supply the '--help' option to see a full list of options for each example.  
#  
# 5. Edit the xml descriptions in the ~/catalog directory to alter the  
# simulated models as desired.  
#  
FROM ubuntu:16.04  
MAINTAINER tom.g.close@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=C.UTF-8  
RUN apt-get update; apt-get install -y build-essential autoconf automake
libtool libreadline6-dev \  
libncurses5-dev libgsl0-dev python-dev python3-dev openmpi-bin libopenmpi-dev
inkscape \  
libhdf5-serial-dev libyaml-dev python3-pip python3-tk python-pip wget zip
unzip flex bison vim nano emacs git  
  
# Update python packages  
RUN pip3 install --upgrade pip  
RUN pip3 install --upgrade virtualenvwrapper  
  
# Add non-root user  
RUN useradd -ms /bin/bash docker  
ENV HOME=/home/docker  
  
# Copy pype9 repo to docker container  
RUN mkdir -p $HOME/packages  
ADD . $HOME/packages/pype9  
RUN chown -R docker:docker $HOME/packages  
  
# Switch to non-root user  
USER docker  
  
# Set up virtualenv  
ENV VIRTUALENVWRAPPER_PYTHON /usr/bin/python3  
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh; mkvirtualenv
pype9"  
ENV VENV /home/docker/.virtualenvs/pype9  
ENV VENV_PIP $VENV/bin/pip  
  
# Install some useful Python packages into the virtualenv  
RUN $VENV_PIP install ipython nose  
  
# Install Neuron and NEST  
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh; workon pype9;
$HOME/packages/pype9/install/nest.sh 2.14.0"  
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh; workon pype9;
$HOME/packages/pype9/install/neuron.sh tag-1665alpha"  
  
# Install 9ML catalog as local git repo for easy editing  
RUN git clone https://github.com/INCF/nineml-catalog.git
$HOME/packages/nineml-catalog  
RUN $VENV_PIP install -e $HOME/packages/nineml-catalog  
RUN ln -s $HOME/packages/nineml-catalog/ninemlcatalog/catalog $HOME/catalog  
  
# Install Pype9 package  
RUN $VENV_PIP install -e $HOME/packages/pype9[plot]  
  
# Manually ensure that NMODL files have been compiled in PyNN installation  
WORKDIR $VENV/lib/python3.5/site-packages/pyNN/neuron/nmodl  
RUN $VENV/bin/nrnivmodl  
WORKDIR $HOME  
  
# Set up matplotlib environemnt  
RUN mkdir -p .config/matplotlib  
RUN echo "backend: Agg" >> .config/matplotlib/matplotlibrc  
  
# Set up bashrc vimrc and add welcome message  
RUN sed 's/#force_color_prompt/force_color_prompt/' $HOME/.bashrc > $HOME/tmp;
mv $HOME/tmp $HOME/.bashrc;  
RUN echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3"  
RUN echo "source /usr/local/bin/virtualenvwrapper.sh" >> $HOME/.bashrc  
RUN echo "workon pype9" >> $HOME/.bashrc  
RUN echo "echo \"Type 'pype9 help' for instructions on how to run pype9\"" >>
$HOME/.bashrc  
RUN echo "echo \"See $HOME/catalog for example 9ML models\"" >> $HOME/.bashrc  
RUN echo "set background=dark" >> $HOME/.vimrc  
RUN echo "syntax on" >> $HOME/.vimrc  
RUN echo "set number" >> $HOME/.vimrc  
RUN echo "set autoindent" >> $HOME/.vimrc  

