FROM simbelmas/fedora-pulse  
RUN dnf -y install funguloids \  
&& dnf -y install mesa-dri-drivers \  
&& dnf clean all  
  
COPY run.sh /run.sh  
RUN chmod a+x /run.sh  
  
ENV HOME /home/svc  
  
ENTRYPOINT /run.sh  

