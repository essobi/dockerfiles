FROM centos:centos7  
MAINTAINER Trevor R.H. Clarke <tclarke@ball.com>  
  
ARG opticks_version=4.12.0  
ARG opticks_rpm=opticks-${opticks_version}-3.x86_64-noldap.rpm  
ARG
opticks_url="https://opticks.org/downloads/opticks/${opticks_version}/${opticks_rpm}"  
ARG spectral_version=1.9.0  
ARG spectral_url="https://opticks.org/downloads/spectral-
processing/${spectral_version}/Spectral-${spectral_version}-linux.aeb"  
VOLUME /wizards  
  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm \  
&& yum install -y
https://opticks.org/downloads/opticks/${opticks_version}/${opticks_rpm} \  
&& yum clean all  
  
ADD ${spectral_url} /opt/Opticks/Extensions/AutoInstall/  
RUN /opt/Opticks/Bin/OpticksBatch  
  
# by default, run /wizards/wizard.batchwiz  
# to run a different wizard or command, add run arguments  
# to run the GUI version of opticks: run -d -e DISPLAY=host-ip:0 --entrypoint
/opt/Opticks/Bin/Opticks opticks  
ENTRYPOINT ["/opt/Opticks/Bin/OpticksBatch"]  
CMD ["-input:/wizards/wizard.batchwiz"]  

