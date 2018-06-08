#  
# Install Topfarm on a fusedwind image.  
# This image depends of the following docker images:  
# - ubuntu:14.10  
# - piredtu/openmdao  
# - piredtu/fusedwind  
#  
# To run with topfarm you first have to activate the relevant virtual  
# environment:  
#  
# $ . /install/openmdao-0.10.3.2/bin/activate  
# $ python foo.py  
#  
FROM piredtu/fusedwind  
  
MAINTAINER Pierre-Elouan Rethore <pire@dtu.dk>  
  
RUN apt-get install -y \  
libfreetype6-dev \  
libpng12-dev \  
python-matplotlib  
  
WORKDIR /install  
  
# Install IpOpt  
ADD install_ipopt.sh /install/  
RUN chmod a+x /install/install_ipopt.sh  
RUN /install/install_ipopt.sh  
  
RUN apt-get install -y \  
cython  
  
# Install windflow  
ADD install_windflo.sh /install/  
RUN chmod a+x /install/install_windflo.sh  
RUN /install/install_windflo.sh  
  
RUN apt-get install -y \  
swig \  
libxft-dev  
  
# Install Topfarm  
ADD install_topfarm.sh /install/  
RUN chmod a+x /install/install_topfarm.sh  
RUN /install/install_topfarm.sh  
  
# Cleaning up all the unnecessary packages  
#RUN apt-get purge -y \  
# build-essential \  
# curl \  
# make \  
# gfortran \  
# subversion \  
# wget  
RUN apt-get autoremove -y  
# Clear package repository cache  
RUN apt-get clean all  
  
ADD . /install  
  
#RUN chmod a+x /install/activate.sh  
#ENTRYPOINT top -b  
CMD /bin/bash  

