FROM fedora:rawhide  
  
ADD setup /  
  
RUN dnf -y install sudo && sh setup-voms-user.sh  
  
RUN /bin/bash setup.sh  
  
USER voms  
WORKDIR /home/voms  
CMD /bin/bash /run.sh  
EXPOSE 15000  

