FROM vmware/photon  
  
ADD pkg/VMware-Log-Insight-Agent-3.0.0-2985111.rpm /tmp/vmware-liagent.rpm  
  
RUN tdnf -y install chkconfig ; \  
tdnf -y install procps-ng ; \  
tdnf -y install sed ;\  
rpm -i -ivf /tmp/vmware-liagent.rpm  
  
ADD pkg/run.sh /tmp/run.sh  
  
RUN chmod 755 /tmp/run.sh  
  
CMD /tmp/run.sh  

