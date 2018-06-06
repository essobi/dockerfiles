FROM ubuntu:latest  
  
MAINTAINER Ivan E. Cao-Berg <icaoberg@andrew.cmu.edu>  
LABEL Author="icaoberg"  
LABEL Laboratory="Murphy Lab"  
LABEL Department="Computational Biology Department"  
LABEL University="Carnegie Mellon University"  
LABEL Vendor="Murphy Lab in the Computational Biology Department at Carnegie
Mellon University"  
LABEL Description="OMERO.searcher local client over Docker."  
LABEL Version="1.3"  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update --fix-missing  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y build-essential git python python-dev python-setuptools
nginx supervisor bcrypt libssl-dev libffi-dev libpq-dev vim redis-server
rsyslog wget  
RUN apt-get install -y python-numpy python-scipy python-matplotlib tree  
RUN apt-get install -y libfreeimage-dev  
RUN easy_install pip  
RUN pip install ipython  
RUN pip install Pillow  
RUN pip install mahotas==0.6.6  
RUN pip install pyslic==0.6.1  
RUN pip install git+git://github.com/icaoberg/ricerca.git  
  
# Configure environment  
ENV SHELL /bin/bash  
ENV USERNAME murphylab  
ENV UID 1000  
RUN useradd -m -s /bin/bash -N -u $UID $USERNAME  
RUN if [ ! -d /home/$USERNAME/ ]; then mkdir /home/$USERNAME/; fi  
WORKDIR /home/murphylab  
USER $USERNAME  
  
# Get OMERO.searcher local client  
RUN wget -nc
http://murphylab.web.cmu.edu/software/searcher/omero.searcher.client-v1.3.tgz  
RUN tar -xf omero.searcher.client-v1.3.tgz  
RUN rm -f omero.searcher.client-v1.3.tgz  
RUN rm -rf ./omero.searcher.client-v1.3/ricerca  
RUN rm -rf ./omero.searcher.client-v1.3/pyslic  
RUN cd ./omero.searcher.client-v1.3 && bash ./tests/test_HPA_slf34.sh

