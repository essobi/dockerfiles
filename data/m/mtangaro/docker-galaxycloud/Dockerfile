FROM mtangaro/docker-centos-epel  
#FROM centos:7.4.1708  
MAINTAINER ma.tangaro@ibiom.cnr.it  
  
ENV container docker  
  
COPY ["playbook.yaml","/"]  
  
RUN ansible-galaxy install indigo-dc.galaxycloud,devel  
  
RUN echo "localhost" > /etc/ansible/hosts  
  
RUN ansible-playbook /playbook.yaml  
  
EXPOSE 21 22 80  
# Start Galaxy and keep it running in background mode  
CMD /usr/local/bin/galaxy-startup; /usr/bin/sleep infinity  

