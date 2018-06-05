FROM gapsystem/gap-docker-base  
  
MAINTAINER The GAP Group <support@gap-system.org>  
  
# Prerequirements  
RUN sudo apt-get update -qq \  
&& sudo apt-get -qq install -y \  
# for ANUPQ package to build in 32-bit mode  
gcc-multilib \  
# for ZeroMQ package  
libzmq3-dev python3-pip  
  
RUN sudo pip3 install notebook jupyterlab_launcher jupyterlab traitlets
ipython vdom  
  
RUN cd /home/gap/inst/ \  
&& rm -rf gap-4.9.1 \  
&& wget -q https://github.com/gap-system/gap/archive/master.zip \  
&& unzip -q master.zip \  
&& rm master.zip \  
&& cd gap-master \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& mkdir pkg \  
&& cd pkg \  
&& wget -q https://www.gap-system.org/pub/gap/gap4pkgs/packages-master.tar.gz
\  
&& tar xzf packages-master.tar.gz \  
&& rm packages-master.tar.gz \  
&& ../bin/BuildPackages.sh \  
&& git clone https://github.com/gap-packages/JupyterKernel.git \  
&& cd JupyterKernel \  
&& python3 setup.py install --user  
  
RUN jupyter serverextension enable \--py jupyterlab --user  
  
ENV PATH /home/gap/inst/gap-master/pkg/JupyterKernel/bin:${PATH}  
ENV JUPYTER_GAP_EXECUTABLE /home/gap/inst/gap-master/bin/gap.sh  
  
# Set up new user and home directory in environment.  
# Note that WORKDIR will not expand environment variables in docker versions <
1.3.1.  
# See docker issue 2637: https://github.com/docker/docker/issues/2637  
USER gap  
ENV HOME /home/gap  
ENV GAP_HOME /home/gap/inst/gap-master  
ENV PATH ${GAP_HOME}/bin:${PATH}  
  
# Start at $HOME.  
WORKDIR /home/gap  
  
# Start from a BASH shell.  
CMD ["bash"]  

