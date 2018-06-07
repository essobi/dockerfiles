FROM fedora:latest  
  
ENV container docker  
  
RUN dnf -y install git gcc-c++ make  
RUN dnf -y install nodejs && \  
npm install -g webpack yarn && \  
dnf -y install yum-utils  
  
CMD [ "/usr/bin/bash" ]  

