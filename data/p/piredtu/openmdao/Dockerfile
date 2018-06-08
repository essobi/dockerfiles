#  
# Install two versions of OpenMDAO (0.10.3.2 and 0.12.0) on a clean ubuntu
image  
# installed virtual environments are in /install/openmdao-xx.xx.xx directories  
#  
# To run with openmdao you first have to activate the relevant virtual  
# environments. For example:  
#  
# $ . /install/openmdao-0.10.3.2/bin/activate  
# $ python foo.py  
#  
FROM ubuntu:15.10  
MAINTAINER Pierre-Elouan Rethore <pire@dtu.dk>  
  
RUN apt-get update && apt-get install -y -q \  
build-essential \  
curl \  
make \  
gfortran \  
git \  
python-dev \  
python-pip \  
python-numpy \  
python-scipy \  
subversion \  
wget  
  
#RUN apt-get update && apt-get build-dep -y \  
# python-numpy \  
# python-scipy  
RUN pip install --upgrade pip  
RUN pip install virtualenv  
#RUN pip install numpy  
#RUN pip install scipy  
WORKDIR /install  
  
# Install OpenMDAO 0.10.3.2  
RUN pip install requests==2.2.1  
RUN curl http://openmdao.org/releases/0.10.3.2/go-openmdao-0.10.3.2.py |
python2  
  
# Install OpenMDAO 0.12.0  
RUN curl http://openmdao.org/releases/0.12.0/go-openmdao-0.12.0.py | python2  
  
# Clear package repository cache  
RUN apt-get autoremove -y  
RUN apt-get clean all  
  
ADD o10.3 /bin/  
RUN chmod +x /bin/o10.3  
  
CMD /bin/bash  

