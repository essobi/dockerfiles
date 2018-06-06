FROM debian:jessie  
  
LABEL maintainer="frank.foerster@ime.fraunhofer.de"  
LABEL description="Dockerfile providing clipper"  
  
RUN apt update && apt install --yes git python build-essential swig python-
scipy python-numpy cython python-setuptools zlib1g-dev libbz2-dev liblzma-dev
python-matplotlib python-pip  
RUN pip install pybedtools pandas  
RUN git clone https://github.com/YeoLab/clipper.git /tmp/clipper  
RUN cd /tmp/clipper && git checkout 1.2 && python setup.py install  

