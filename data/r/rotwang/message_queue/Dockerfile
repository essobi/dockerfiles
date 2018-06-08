FROM ansible/ubuntu14.04-ansible:latest  
  
ADD / /root/  
RUN ansible-playbook -i /root/local/hosts.ini /root/install.yml  
  
# quick and dirty, ideally we would "unpack" ansible to this dockerfile  
USER affinitas_chat  
ENTRYPOINT
["/opt/affinitas_chat/apollomq_1.7.1/chat.elitesingles.com/bin/apollo-broker"]  
CMD ["run"]  
  

