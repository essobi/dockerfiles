FROM ubuntu:16.04  
MAINTAINER Guilhem Lettron <guilhem@lettron.fr>  
  
ADD https://staticdownloads.site24x7.com/server/Site24x7_Linux_64bit.install
/install  
  
RUN tail -n +$(grep -m1 INSTALL_FILE_LENGTH /install | sed 's/.*=//') /install
> /install.tar && \  
mkdir -p /opt/site24x7 && \  
tar xf /install.tar -C /opt/site24x7 && \  
rm -f /install.tar  
  
CMD ["/opt/site24x7/monagent/lib/Site24x7Agent"]  

