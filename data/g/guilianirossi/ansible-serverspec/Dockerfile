FROM ansible/ubuntu14.04-ansible  
MAINTAINER "Rossi Guiliani" <rossi@guiliani.me>  
  
ADD ./provisioning /mnt  
RUN ansible-playbook -c local -i localhost, /mnt/build.yaml  

