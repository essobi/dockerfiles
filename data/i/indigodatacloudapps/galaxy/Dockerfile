FROM indigodatacloud/centos-sshd:7  
MAINTAINER ma.tangaro@gmail.com  
  
ENV container docker  
  
COPY ["playbook.yaml","/"]  
  
RUN ansible-galaxy install indigo-dc.galaxycloud  
  
RUN echo "localhost" > /etc/ansible/hosts  
  
RUN ansible-playbook /playbook.yaml  
  
EXPOSE 21 22 80  
CMD /etc/init.d/vmcontext start; /usr/bin/galaxy-startup; /usr/sbin/sshd -D  

