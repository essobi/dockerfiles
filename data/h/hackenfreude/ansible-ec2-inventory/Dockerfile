FROM python:2  
RUN pip install ansible==2.2.1.0  
  
RUN pip install boto==2.46.1  
  
RUN curl --create-dirs -o /etc/ansible/hosts
https://raw.githubusercontent.com/ansible/ansible/v2.2.1.0-1/contrib/inventory/ec2.py  
  
RUN chmod +x /etc/ansible/hosts  
  
CMD [ "bash" ]  

