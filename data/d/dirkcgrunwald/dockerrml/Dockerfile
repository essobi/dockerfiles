FROM ubuntu:14.04  
MAINTAINER Tim O'Shea <tim.oshea753@gmail.com>  
  
# set up environment  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set prefix variables  
ENV PyBOMBS_init /gr/  
# Update apt-get  
RUN apt-get update  
  
# Install PyBOMBS dependencies  
RUN apt-get update && \  
apt-get install -y \  
python-pip \  
python-yaml \  
python-setuptools \  
git-core python-software-properties software-properties-common && \  
apt-add-repository -y ppa:x2go/stable  
  
# Add recipes to PyBOMBS  
RUN pip install pyBOMBS && \  
pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git
&& \  
pybombs recipes add gr-etcetera git+https://github.com/gnuradio/gr-
etcetera.git  
# Setup environment  
RUN pybombs prefix init ${PyBOMBS_init} && \  
echo "source "${PyBOMBS_init}"/setup_env.sh" > /root/.bashrc  
# Setup packages which should be installed by PyBOMBS  
ENV packages "gnuradio gr-burst gr-pyqt gr-pcap gr-mapper gr-analysis "  
# Update apt-get  
RUN apt-get update && \  
pybombs -v install \--deps-only ${packages} && rm -rf ${PyBOMBS_init}/src/*  
  
# Install previously selected packages and clean-up unused source  
RUN pybombs -v install \--no-deps ${packages} && rm -rf ${PyBOMBS_init}/src/*  
  
# install core packages  
RUN apt-get update && \  
apt-get install -y python-pip git openssh-server vim emacs screen tmux locate
\  
python-matplotlib python-scipy python-numpy \  
python-sklearn python-sklearn-doc python-skimage \  
python-skimage-doc python-scikits-learn python-scikits.statsmodels \  
python-opencv gimp \  
firefox evince audacity meld \  
xfwm4 xfce4 x2goserver x2goserver-xsession \  
autotools-dev autoconf sudo wireshark gdb  
  
# Set up remove login info  
# SSH login fix. Otherwise user is kicked off after login  
  
RUN mkdir /var/run/sshd && \  
(echo 'root:radioml' | chpasswd) && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
  
VOLUME /home/x2go/mnt  
# install python packages  
RUN pip install \--upgrade pip  
RUN pip install \--upgrade ipython[all]  
RUN pip install \--upgrade \--no-deps git+git://github.com/Theano/Theano.git  
RUN pip install \--upgrade
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp27-none-
linux_x86_64.whl  
RUN pip install \--upgrade git+https://github.com/fchollet/keras.git  
RUN pip install \--upgrade seaborn tqdm  
  
# check out sources for reference  
RUN mkdir -p /gr/src && \  
mkdir -p /home/x2go && \  
/bin/ln -s /gr/src/ /home/x2go/src  
RUN cd /home/x2go/src/ && git clone https://github.com/Theano/Theano.git  
RUN cd /home/x2go/src/ && git clone
https://github.com/tensorflow/tensorflow.git  
RUN cd /home/x2go/src/ && git clone https://github.com/fchollet/keras.git  
# Build PyOpenPNL and Gym deps  
RUN pip install networkx  
RUN apt-get install -y python-numpy python-dev cmake \  
zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev \  
python-opengl libboost-all-dev libsdl2-dev swig pypy-dev \  
libtool  
  
RUN cd /home/x2go/src/ && \  
git clone https://github.com/PyOpenPNL/OpenPNL.git && \  
cd OpenPNL && \  
./autogen.sh && \  
./configure CFLAGS='-g -O2 -fpermissive -w' CXXFLAGS='-g -O2 -fpermissive -w'
&& \  
make -j4 && \  
make install  
  
RUN cd /home/x2go/src/ && git clone https://github.com/PyOpenPNL/PyOpenPNL.git
&& cd PyOpenPNL && python setup.py build && python setup.py install  
RUN cd /home/x2go/src/ && git clone https://github.com/osh/kerlym.git && cd
kerlym && python setup.py build && python setup.py install  
  
# set up OpenAI Gym  
RUN cd /home/x2go/src/ && git clone https://github.com/openai/gym.git && cd
gym && pip install -e .  
RUN pip install gym[atari] pachi_py  
RUN mkdir -p /home/x2go/src/notebooks/  
#  
# Add interactive user for x2go  
#  
COPY imagefiles-jupyter /home/x2go/.jupyter  
COPY imagefiles-sudo /etc/sudoers.d  
COPY .vimrc /home/x2go/  
RUN adduser \--gecos "X2Go User" \--disabled-password x2go && \  
(echo "x2go:x2go" | chpasswd) && \  
mkdir -p /home/x2go/.jupyter /home/x2go/mnt && \  
echo "source /gr/setup_env.sh" >> /home/x2go/.bashrc  
  
WORKDIR /home/x2go  
  
  
RUN apt-get install -y supervisor  
COPY imagefiles-supervisord /etc/supervisor/conf.d  
  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN chown -R x2go /home/x2go  
  
EXPOSE 22 8888  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]  

