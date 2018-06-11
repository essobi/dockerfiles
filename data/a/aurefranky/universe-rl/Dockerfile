# DOCKER CONTAINER FOR PRODUCTION  
FROM tensorflow/tensorflow:latest  
  
MAINTAINER Tiancong Zheng <tiancong.zheng@ericsson.com>  
MAINTAINER Jesper Derehag <jesper.derehag@ericsson.com>  
MAINTAINER Aurelien Hontabat <aurelien.hontabat@ericsson.com>  
  
RUN mkdir -p /usr/src/dist  
RUN mkdir -p /usr/src/dist/rl  
  
RUN add-apt-repository ppa:ubuntu-lxc/lxd-stable  
RUN apt-get update  
RUN apt-get install -y swig cmake python-opencv zlib1g-dev git-core golang
libjpeg-turbo8-dev make  
COPY pip-requirements.txt /usr/src/dist  
RUN cd /usr/src/dist && pip install -r pip-requirements.txt  
RUN git clone https://github.com/openai/universe.git && cd universe && pip
install -e .  
RUN pip install gym[atari]  
  
COPY tools /usr/src/dist/tools  
COPY util /usr/src/dist/util  
COPY rl/dqn.py /usr/src/dist/rl  
COPY rl/__init__.py /usr/src/dist/rl  
COPY run_game.py /usr/src/dist  
COPY docker-entrypoint.sh /usr/src/dist  
  
WORKDIR /usr/src/dist  
  
EXPOSE 6006  
ENTRYPOINT ["sh", "docker-entrypoint.sh"]  

