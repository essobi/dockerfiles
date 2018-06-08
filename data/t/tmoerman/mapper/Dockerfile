FROM ubuntu:14.04  
  
MAINTAINER Thomas Moerman (https://twitter.com/thomasjmoerman)  
  
RUN apt-get -y update \  
&& sudo apt-get install -y wget python-setuptools \  
python-numpy python-scipy python-matplotlib python-wxtools \  
python-opengl graphviz libboost-all-dev mercurial \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tools  
  
RUN hg clone http://danifold.net/hg/mapper  
  
RUN cd mapper/cmappertools \  
&& python setup.py install --user  
  
RUN wget
https://pypi.python.org/packages/source/f/fastcluster/fastcluster-1.1.13.tar.gz
\  
&& tar -xf fastcluster-1.1.13.tar.gz \  
&& cd fastcluster-1.1.13 \  
&& python setup.py install --user \  
&& cd .. \  
&& rm fastcluster-1.1.13.tar.gz \  
&& rm -r fastcluster-1.1.13/  
  
CMD cd mapper && python bin/MapperGUI.py

