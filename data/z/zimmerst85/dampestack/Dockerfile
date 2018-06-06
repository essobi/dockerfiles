FROM centos:6.6  
MAINTAINER Stephan Zimmer <zimmer@slac.stanford.edu>  
### adding yum plugin for overlayfs  
RUN yum -y install yum-plugin-ovl && yum clean all  
RUN yum -y install tar  
### adding pip for python  
RUN yum -y install epel-release  
RUN yum -y install python-pip  
### add workflow  
ADD requirements /tmp/requirements  
RUN for pkg in $(cat /tmp/requirements); do echo "installing package ${pkg}";
pip install ${pkg}; done  
RUN curl -o workflow.tar.gz -L -k
https://dampevm3.unige.ch/dmpworkflow/releases/DmpWorkflow.devel.tar.gz && tar
xzvf workflow.tar.gz && mv DmpWorkflow* DmpWorkflow  
RUN echo "export PYTHONPATH=/DmpWorkflow/:${PYTHONPATH}" >> /root/.bashrc  
RUN mkdir -p /apps/  
ADD dampe-cli-update-job-status /apps/  
RUN echo "export PATH=/apps:${PATH}" >> /root/.bashrc  
### adding cvmfs  
RUN yum -y install https://ecsft.cern.ch/dist/cvmfs/cvmfs-release/cvmfs-
release-latest.noarch.rpm && yum clean all  
RUN yum -y install cvmfs cvmfs-config-default --nogpgcheck && yum clean all  
RUN cvmfs_config setup  
ADD default.local /etc/cvmfs/default.local  
RUN mkdir -p /cvmfs/dampe.cern.ch  
### ROOT prerequisites  
RUN yum -y install git cmake gcc-c++ gcc binutils libX11-devel libXpm-devel
libXft-devel libXext-devel && yum clean all  
### more prerequisites  
RUN yum -y install mesa-libGLU-devel libXmu-devel && yum clean all  
RUN echo "mount -t cvmfs dampe.cern.ch /cvmfs/dampe.cern.ch" >> /root/.bashrc  
RUN echo "source /cvmfs/dampe.cern.ch/rhel6-64/etc/setup.sh" >> /root/.bashrc  
ADD docker.cfg /DmpWorkflow/DmpWorkflow/config/settings.cfg  
ENTRYPOINT ["/bin/bash","--login","-c"]

