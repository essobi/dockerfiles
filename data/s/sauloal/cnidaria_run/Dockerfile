FROM sauloal/cnidaria_make_env  
  
RUN apt-get update && \  
apt-get install -y python python-setuptools \  
python-numpy python-pandas python-matplotlib \  
python-cogent python-imaging python-qt4 \  
python-pip python-lxml && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#python-mpi4py  
  
RUN easy_install ete2 && easy_install hcluster && easy_install bitarray  

