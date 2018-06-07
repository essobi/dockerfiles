FROM vmware/photon  
  
  
RUN tdnf -y install apache-maven ; \  
tdnf -y install git ; \  
tdnf -y install openjdk ;\  
mkdir /var/build  
  
ADD run.sh /var/build  
  
CMD sh /var/build/run.sh

