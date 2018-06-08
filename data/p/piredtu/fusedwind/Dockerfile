FROM piredtu/openmdao  
  
MAINTAINER Pierre-Elouan Rethore <pire@dtu.dk>  
  
WORKDIR /install  
  
# Install  
ADD install_fusedwind.sh /install/  
RUN chmod a+x /install/install_fusedwind.sh  
RUN /install/install_fusedwind.sh  
  
RUN apt-get autoremove -y  
# Clear package repository cache  
RUN apt-get clean all  
  
ADD . /install  
CMD /bin/bash  

