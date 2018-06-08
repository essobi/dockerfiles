FROM gesellix/ansible:2.1.2.0  
ENV ANSIBLE_VAULT_PASSWORD_FILE=/vault.key  
  
WORKDIR /ansible  
ADD ./known_hosts /root/.ssh/known_hosts  
ADD . /ansible  
  
CMD ["ansible", "--version"]  

