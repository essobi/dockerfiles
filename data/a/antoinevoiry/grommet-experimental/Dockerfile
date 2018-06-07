FROM node:0.12.7-wheezy  
  
# remove several traces of debian python  
RUN apt-get purge -y python.*  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# install GULP and GROMMET  
RUN \  
npm install -g bower gulp --save-dev && \  
npm link gulp && \  
npm install -g grommet  
  
# Define working directory.  
WORKDIR /data  
  
# replace this with your application's default port  
EXPOSE 9000  
# Define default command.  
#CMD ["bash"]  

