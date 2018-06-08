FROM nlesc/xenon-slurm-abstract  
  
WORKDIR /usr/local  
  
# download, compile and install slurm  
RUN /bin/bash install_slurm.sh slurm-14-11-11-1.tar.gz  
  
# ADD slurm.conf from context to sysconfig directory  
ADD slurm.conf /usr/local/etc/slurm/slurm.conf  
  
# set the work directory to something sane  
WORKDIR /home/xenon/  
  

