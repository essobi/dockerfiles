FROM vmware/photon  
  
  
RUN tdnf -y install git ; \  
mkdir /var/build  
  
ADD run.sh /var/build  
  
CMD sh /var/build/run.sh

