FROM ubuntu:xenial  
MAINTAINER Ian Hinder <ian.hinder@aei.mpg.de>  
  
RUN apt-get update && apt-get install -y openssh-server openjdk-9-jre-headless
git nano build-essential git gfortran mpich libhdf5-serial-dev libfftw3-dev
libgsl0-dev libssl-dev liblapack-dev hdf5-tools ccache pkg-config texlive-
latex-extra tex4ht locales && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
  
RUN useradd -d "/home/jenkins" -u 1000 -m -s /bin/bash jenkins  
  
USER jenkins  
  
RUN mkdir /home/jenkins/.ssh && chmod g=,o= /home/jenkins/.ssh  
  
ADD authorized_keys /home/jenkins/.ssh/authorized_keys  
  
USER root  
  
RUN chown jenkins:jenkins /home/jenkins/.ssh/authorized_keys && chmod g=,o=
/home/jenkins/.ssh/authorized_keys  
  
RUN locale-gen en_US.UTF-8 en_IE.UTF-8  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

