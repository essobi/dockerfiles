FROM ubuntu:16.04  
MAINTAINER Manuel Kaufmann <humitos@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y \  
python-setuptools \  
python-qt4 \  
python-qt4-gl \  
git-core \  
python-qt4-phonon \  
build-essential \  
python-dev \  
swig \  
subversion \  
python-pygame \  
python-pip  
  
RUN pip install --upgrade pip  
RUN pip install box2d  
  
RUN adduser --quiet --disabled-password pilas  
  
RUN git clone http://github.com/hugoruscitti/pilas /code \  
&& cd /code \  
&& git checkout 1.4.11  
  
WORKDIR /code  
  
CMD ./bin/pilasengine  

