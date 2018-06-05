#################################################################################  
#  
# Docker for CI buildups connected to private DIRAC GitLab repo  
#  
# Written by Miro Ilias, GSI/Darmstadt, August-September,2017  
#  
#################################################################################  
#  
#  
# we have LTS Ubuntu  
FROM ubuntu:16.04  
#  
RUN apt-get update  
RUN apt-get install -y sudo  
# remove locks, fix management of packages  
RUN rm -rf /var/lib/apt/lists/* && sudo rm /var/cache/apt/archives/lock  
RUN sudo dpkg --configure -a  
# needs CMake (some problems with this package)  
RUN sudo apt-get update  
RUN sudo apt-get install -y cmake  
# adds Python package  
RUN sudo apt-get install -y python  
# install git package  
RUN sudo apt-get install -y git  
# needs Fortran,C, C++  
RUN sudo apt-get install -y gcc g++ gfortran  
RUN sudo apt-get install -y zlib1g-dev  
# remove OpenMPI and install MPICH parallelization libraries  
RUN sudo apt-get remove openmpi-bin libopenmpi-dev  
RUN sudo apt-get install -y mpich  
# clean packages at the end  
RUN sudo apt-get autoclean  
RUN sudo apt-get clean  
RUN sudo apt-get autoremove  

