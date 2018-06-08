# [START all]  
# Create an enhanced and K8s-friendly Super NetOps container  
FROM f5devcentral/f5-super-netops-container:ansible  
  
# create directories necessary for f5-ansible setup  
RUN rm -rf /usr/share/ansible  
RUN mkdir /usr/share/ansible  
RUN mkdir ~/ansible  
RUN mkdir ~/ansible/playbooks/  
RUN mkdir ~/ansible/playbooks/files/  
  
# dowload the playbooks  
WORKDIR ~/ansible/playbooks  
RUN wget
https://raw.githubusercontent.com/mlowcher61/F5-Ansible/master/f5_ansible_setup.yml  
RUN wget
https://raw.githubusercontent.com/mlowcher61/F5-Ansible/master/enable_appconnector.yml  
RUN wget
https://raw.githubusercontent.com/mlowcher61/F5-Ansible/master/appconnector_vips.yml  
RUN wget
https://raw.githubusercontent.com/mlowcher61/F5-Ansible/master/acproxy_install.yml  
RUN wget
https://raw.githubusercontent.com/mlowcher61/F5-Ansible/master/appconn_monitor.yml  
  
# demonstrate that the above ran  
RUN ls -lR /usr/share/ansible ~  
  
# [END all]  

