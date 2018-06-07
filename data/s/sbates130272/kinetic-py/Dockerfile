#  
# kinetic-sim Dockerfile  
#  
# https://github.com/sbates130272/docker-kinetic-py  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# Set the maintainer  
MAINTAINER Stephen Bates (sbates130272) <sbates@raithlin.com>  
  
# Install the Seagate/kinetic-py code from Github, we also need  
# git and python and some python add-ins so we install them too.  
# Since this container may well run in interactive mode we also  
# install things like emacs and ipython. As per Dockerfile best  
# practices we split this up to get snapshots along the way.  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y python  
RUN apt-get install -y python-dev  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-setuptools  
RUN apt-get install -y emacs  
RUN pip install ipython  
RUN git clone https://github.com/Seagate/kinetic-py.git  
  
# Now cd into the working folder and setup and install the API  
# module. Note we do this on the same RUN comma  
WORKDIR kinetic-py  
RUN git submodule update --init  
RUN python setup.py develop  
  
# Now cd back to the top-level folder and grab the  
# sbates130272/kinetic repo which contains a codebase for working with  
# the kinetic HDDs.  
WORKDIR ..  
git clone https://github.com/sbates130272/kinetic.git  
WORKDIR kinetic  
  

