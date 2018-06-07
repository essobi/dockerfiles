FROM spiffylogic/chat-ping-centos-ansible-base  
MAINTAINER Carlos Feliz <carlos@spiffylogic.com>  
ENV REFRESHED_AT 03-18-2016  
LABEL version="1.2"  
  
ADD ./machine.py /machine.py  
ADD ./playbooks /playbooks  
ADD ./conf/ansible.cfg /etc/ansible/ansible.cfg  
ADD ./entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["/playbooks/bootstrap.yml"]  

