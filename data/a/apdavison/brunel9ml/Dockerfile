#  
# A Docker image for running NineML demonstrations using both  
# (i) the Python toolchain with NEURON  
# (ii) the 9ML-toolkit utility (Chicken Scheme)  
#  
# To build:  
# docker build -t ninemldemo .  
#  
# To run:  
#  
# mkdir myresults  
# docker run -v `pwd`/myresults:/home/docker/projects/ninemldemo/results -t -i
ninemldemo /bin/bash  
#  
# (the -v flag specifies a local directory that will be shared with the Docker
container,  
# so you can easily access simulation results on the host computer).  
FROM neuralensemble/simulation:py2  
MAINTAINER andrew.davison@unic.cnrs-gif.fr  
  
RUN sed 's/#force_color_prompt/force_color_prompt/' .bashrc > tmp; mv tmp
.bashrc  
RUN echo "source /home/docker/env/neurosci/bin/activate" >> .bashrc  
  
USER root  
RUN apt-get update; apt-get install -y python-lxml python-pandas libgmp-dev  
USER docker  
  
# For simulation we require Neo 0.3.3, for analysis we need the development  
# version of Neo. We therefore create a second virtualenv for analysis  
ENV VENV2=$HOME/env/analysis  
RUN virtualenv --system-site-packages $VENV2  
RUN $VENV2/bin/pip install -U numpy parameters quantities # need numpy >= 1.9  
RUN wget https://github.com/NeuralEnsemble/python-neo/archive/apibreak.tar.gz
-O $HOME/packages/neo_apibreak.tar.gz  
RUN $VENV2/bin/pip install $HOME/packages/neo_apibreak.tar.gz  
RUN $VENV2/bin/pip install elephant  
  
# Install NineML libraries  
WORKDIR $HOME/packages  
RUN echo "change this line to ensure we skip the cache"; git clone
https://github.com/apdavison/lib9ML.git  
RUN git clone https://bitbucket.org/apdavison/ninemlcodegen.git  
RUN git clone https://github.com/apdavison/PyNN.git  
RUN $VENV/bin/pip install ./lib9ML  
RUN $VENV/bin/pip install ./ninemlcodegen/nmodl  
RUN cd ./PyNN; git checkout nineml; $VENV/bin/pip install .  
RUN cd $VENV/local/lib/python2.7/site-packages/pyNN/neuron/nmodl;
$VENV/bin/nrnivmodl  
RUN $VENV/bin/pip install sarge  
  
# Install the 9ML toolkit  
RUN wget http://code.call-cc.org/releases/4.11.0/chicken-4.11.0.tar.gz  
RUN tar zxf chicken-4.11.0.tar.gz; cd chicken-4.11.0; make PLATFORM=linux
PREFIX=$HOME/chicken install  
RUN $HOME/chicken/bin/chicken-install 9ML-toolkit  
RUN ln -s $HOME/chicken/bin/9ML-network $VENV/bin  
  
RUN wget
http://downloads.sourceforge.net/project/mlton/mlton/20130715/mlton-20130715-1.amd64-linux.tgz?use_mirror=heanet
-O mlton-20130715-1.amd64-linux.tgz  
RUN tar xzf mlton-20130715-1.amd64-linux.tgz; mv usr/lib/mlton $VENV/lib; mv
usr/bin/* $VENV/bin  
RUN sed "s%lib='/usr/lib/mlton'%lib=\$VENV/lib/mlton%" $VENV/bin/mlton >
mlton.tmp; mv mlton.tmp $VENV/bin/mlton  
RUN chmod u+x $VENV/bin/mlton  
  
# Install the Brunel (2000) project directory  
RUN mkdir $HOME/projects  
WORKDIR $HOME/projects  
##RUN echo "change this text to ensure we skip the cache"; git clone
https://apdavison@bitbucket.org/apdavison/nineml_demo_2016.git  
##WORKDIR $HOME/projects/nineml_demo_2016  
# Clone the 9ML-toolkit and copy the examples directories  
##RUN git clone https://github.com/iraikov/9ML-toolkit.git  
# Welcome message  
RUN echo 'echo "Docker container for running NineML demonstrations. See
README.rst for instructions."' >> $HOME/.bashrc  
  
# TODO: link the results directories to the shared "myresults" directory.
Symbolic links? or modify scripts?

