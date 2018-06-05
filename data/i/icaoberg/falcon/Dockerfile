FROM ubuntu:latest  
  
MAINTAINER Ivan E. Cao-Berg <icaoberg@alumni.cmu.edu>  
LABEL Description="FALCON for Python over Docker. halcon is a python
implementation of the Feedback Adaptive Loop for Content-Based Retrieval
(FALCON) algorithm."  
LABEL Vendor="Computational Biology Department at Carnegie Mellon University"  
LABEL Version="0.1"  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN apt-get install -y build-essential git python python-dev python-setuptools
nginx supervisor bcrypt libssl-dev libffi-dev libpq-dev vim redis-server
rsyslog wget  
RUN apt-get install -y python-numpy python-scipy python-matplotlib  
RUN easy_install pip  
RUN pip install sphinx  
RUN pip install tabulate  
RUN pip install halcon  
  
# Configure environment  
ENV DEBIAN_FRONTEND noninteractive  
ENV SHELL /bin/bash  
ENV USERNAME icaoberg  
ENV UID 1000  
RUN useradd -m -s /bin/bash -N -u $UID $USERNAME  
RUN if [ ! -d /home/$USERNAME/ ]; then mkdir /home/$USERNAME/; fi  
WORKDIR /home/$USERNAME/  
USER $USERNAME  
  
RUN git clone https://github.com/icaoberg/falcon.git  
RUN git clone https://github.com/icaoberg/falcon-docs.git  

