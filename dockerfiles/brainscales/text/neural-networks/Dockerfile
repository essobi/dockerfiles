#######################################
# Installation of the neural network simulators used in BrainScaleS
# nest, neuron, brian 
# and the common PyNN interface to these simulators
# Installation of the multi-simulation coordinator music
#######################################

FROM jchavas/saucy-sshd

#######################################
# initialization
#######################################
ENV DEBIAN_FRONTEND noninteractive

#######################################
# neural networks simulators
#######################################

#before installing music
RUN apt-get -y install freeglut3 freeglut3-dev binutils-gold
RUN apt-get -y install automake libtool build-essential subversion openmpi-bin libopenmpi-dev


#installation of music
RUN cd /root; svn co --non-interactive --username Anonymous --password Anonymous http://svn.incf.org/svn/music/branches/multiconn music
RUN cd /root/music && ./autogen.sh && ./configure && make && make install

#before installing nest
RUN apt-get -y install wget  python libpython-dev libncurses5-dev libreadline-dev python-matplotlib 
RUN apt-get -y install libgsl0-dev

#nest installation
RUN cd /root; wget http://www.nest-simulator.org/download/gplreleases/nest-2.2.2.tar.gz
RUN cd /root; tar xvzf nest-2.2.2.tar.gz; rm nest-2.2.2.tar.gz
RUN cd /root/nest-2.2.2 && ./configure --with-mpi --prefix=/opt/nest --with-pynest-prefix=/usr
RUN cd /root/nest-2.2.2 && make && make install
RUN echo 'export PATH=$PATH:/opt/nest/bin' >> /etc/bash.bashrc

#to install brian
RUN apt-get -y install python-pip python-scipy ipython
RUN pip install sympy

#brian installation
RUN pip install brian

#to install neuron
RUN apt-get -y install libx11-dev libxext-dev

#neuron installation
RUN cd /root; wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.3/nrn-7.3.tar.gz
RUN cd /root; wget http://www.neuron.yale.edu/ftp/neuron/versions/v7.3/iv-18.tar.gz
RUN cd /opt; mkdir neuron; mv /root/nrn-7.3.tar.gz /root/iv-18.tar.gz neuron/
RUN cd /opt/neuron; tar xzf iv-18.tar.gz; rm iv-18.tar.gz; mv iv-18 iv
RUN cd /opt/neuron/iv; ./configure --prefix=`pwd` && make && make install
RUN cd /opt/neuron; tar xzf nrn-7.3.tar.gz; rm nrn-7.3.tar.gz; mv nrn-7.3 nrn
RUN cd /opt/neuron/nrn; ./configure --prefix=`pwd` --with-nrnpython --with-mpi --with-music=/usr/local && make && make install
RUN echo 'export PATH=$PATH:/opt/neuron/iv/x86_64/bin:/opt/neuron/nrn/x86_64/bin' >> /etc/bash.bashrc
RUN cd /opt/neuron/nrn/src/nrnpython; python setup.py install

#pyNN installation
RUN pip install mpi4py
RUN pip install jinja2 Cheetah csa
RUN PATH=$PATH:/opt/neuron/iv/x86_64/bin:/opt/neuron/nrn/x86_64/bin:/opt/nest/bin pip install pyNN

#######################################
# tests
#######################################

RUN pip install nose mock
RUN cd /root; wget https://pypi.python.org/packages/source/P/PyNN/PyNN-0.7.5.tar.gz; tar xzf PyNN-0.7.5.tar.gz; rm PyNN-0.7.5.tar.gz
RUN export PATH=$PATH:/opt/neuron/iv/x86_64/bin:/opt/neuron/nrn/x86_64/bin:/opt/nest/bin; cd /root/PyNN-0.7.5/test/unittests && nosetests -I test_neuron -I test_nest && nosetests test_nest.py && nosetests test_neuron.py
RUN cd /root/music/test; mpirun -np 4 music /root/music/test/events.music
RUN export PATH=$PATH:/opt/nest/bin; cd /root; files=$(ls /root/nest-2.2.2/testsuite/unittests/*.sli); for f in $files; do nest $f; if [ $? != 0 ]; then echo "ERROR in nest unittests: function $f"; exit 1; fi; done; rm *.dat *.gdf

#######################################
# copying and cleaning
#######################################
ADD README /root/README
RUN unset DEBIAN_FRONTEND


