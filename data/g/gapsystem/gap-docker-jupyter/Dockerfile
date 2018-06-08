FROM gapsystem/gap-docker  
  
MAINTAINER The GAP Group <support@gap-system.org>  
  
#ADD requirements.txt /home/gap/  
RUN sudo apt-get update && \  
sudo apt-get install -y --force-yes \  
build-essential pkg-config \  
python3 python3-dev \  
python3-pip python3-setuptools \  
libfreetype6-dev libpng-dev libjpeg-dev zlib1g-dev \  
&& sudo pip3 install --upgrade setuptools pip \  
&& sudo pip3 install jupyter \  
&& cd /home/gap \  
&& wget -q https://github.com/gap-packages/jupyter-kernel-
gap/archive/v0.9.tar.gz \  
&& tar xzf v0.9.tar.gz \  
&& rm v0.9.tar.gz \  
&& cd jupyter-kernel-gap-0.9 \  
&& sudo python3 setup.py install  
  
# Set up new user and home directory in environment.  
# Note that WORKDIR will not expand environment variables in docker versions <
1.3.1.  
# See docker issue 2637: https://github.com/docker/docker/issues/2637  
USER gap  
ENV HOME /home/gap  
ENV GAP_HOME /home/gap/inst/gap4r8  
ENV PATH ${GAP_HOME}/bin:${PATH}  
ENV JUPYTER_GAP_EXECUTABLE /home/gap/inst/gap4r8/bin/gap.sh  
  
# Start at $HOME.  
WORKDIR /home/gap  
  
EXPOSE 8888  
CMD jupyter notebook --no-browser --ip=0.0.0.0  

