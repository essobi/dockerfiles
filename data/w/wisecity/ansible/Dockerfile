FROM python:2.7  
RUN echo ' StrictHostKeyChecking no' >> /etc/ssh/ssh_config  
RUN pip install ansible -i https://pypi.douban.com/simple  
  
COPY ansible-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/ansible-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["ansible-entrypoint.sh"]  
  
CMD ["ansible-playbook"]  

