FROM indigodatacloud/ubuntu-sshd:14.04  
MAINTAINER Miguel Caballer <micafer1@upv.es>  
  
COPY ["playbook.yaml", "/"]  
  
RUN ansible-galaxy install indigo-dc.eubiosteo  
  
RUN echo "localhost" > /etc/ansible/hosts  
  
RUN ansible-playbook /playbook.yaml  
  
EXPOSE 22  
# CMD /etc/init.d/vmcontext start; /usr/sbin/sshd -D  

