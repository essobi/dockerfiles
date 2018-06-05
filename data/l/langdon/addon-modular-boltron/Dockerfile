FROM registry.fedoraproject.org/fedora-minimal:28  
#RUN sed -i -e 's/gpgcheck=1/gpgcheck=0/g' /etc/yum.repos.d/*  
RUN microdnf update -y && microdnf clean all  
RUN microdnf install -y dnf ansible && microdnf clean all  
RUN mkdir /playbooks/  
COPY semimodular_deployment /playbooks/semimodular_deployment  
COPY semimodular-play.yml /playbooks/  
  
RUN ansible-playbook -i "localhost," -c local /playbooks/semimodular-play.yml  
  
RUN mkdir /local-modules  
ADD start.sh /start.sh  
RUN chmod a+x /start.sh  
VOLUME /local-modules  
CMD /start.sh  

