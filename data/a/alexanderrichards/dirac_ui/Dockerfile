FROM centos:6  
LABEL maintainer "Alexander Richards <a.richards@imperial.ac.uk>"  
ARG dirac_version=v6r17p18  
  
RUN yum install -y wget  
  
# Add the user UID:1000, GID:1000, home at /home/dirac  
RUN groupadd -r dirac -g 1000 && \  
useradd -u 1000 -r -g dirac -m -d /home/dirac -s /sbin/nologin -c "Dirac user"
dirac && \  
chmod 755 /home/dirac  
  
# Set the working directory to dirac home directory  
WORKDIR /home/dirac  
  
# Specify the user to execute all commands below  
USER dirac  
  
RUN mkdir dirac_ui && \  
cd dirac_ui && \  
wget -np -O dirac-install
https://raw.githubusercontent.com/DIRACGrid/DIRAC/integration/Core/scripts/dirac-
install.py && \  
chmod u+x dirac-install && \  
./dirac-install -r $dirac_version -i 27 -g 2017-01-27 && \  
rm -f dirac-install  
  
ENTRYPOINT . dirac_ui/bashrc && \  
dirac-proxy-init -x && \  
dirac-configure -F -S GridPP -C
dips://dirac01.grid.hep.ph.ic.ac.uk:9135/Configuration/Server -I && \  
dirac-proxy-init -g ${vo}_user -M && \  
/bin/bash  

