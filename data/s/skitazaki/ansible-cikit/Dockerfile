FROM python:3.6  
RUN pip install ansible==2.4.3 \  
ansible-lint \  
awscli \  
boto3 boto  
  
CMD ansible-playbook site.yml --syntax-check  

