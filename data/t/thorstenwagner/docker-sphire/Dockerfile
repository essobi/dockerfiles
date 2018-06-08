# SPHIRE Installation  
# Based on CENTOS6  
FROM centos:centos6  
  
MAINTAINER Thorsten Wagner (https://github.com/thorstenwagner)  
  
# this is a non-interactive automated build - avoid some warning messages  
ENV CENTOS_FRONTEND noninteractive  
RUN pwd  
# update repositories  
RUN yum update  
  
# install wget  
RUN yum install wget which mesa-libGL-devel -y  
  
# get sphire  
RUN mkdir SPHIRE-INSTALL  
RUN cd SPHIRE-INSTALL  
RUN pwd  
RUN wget --no-check-certificate
https://ftp.gwdg.de/pub/misc/sphire/sphire_beta_20170602/sphire_beta_20170602.linux64.centos6.sh  
RUN bash sphire_beta_20170602.linux64.centos6.sh -b -p ../SPHIRE  
  
RUN cd ../SPHIRE  
RUN pwd  
RUN echo "PATH=${PWD}/bin:${PATH}" >> ${HOME}/.bashrc  
RUN source ${HOME}/.bashrc  
RUN ls  
RUN bash utils/uninstall_openmpi.sh -y  
RUN bash utils/build_and_install_openmpi.sh  
RUN bash utils/build_pydusa_numpy.sh 1.8 --no-test  
RUN bash utils/install_pydusa_numpy.sh 1.8  
  
# open ssh port  
EXPOSE 22  

