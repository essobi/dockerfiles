FROM python  
MAINTAINER Mathias Gebbe <mathias.gebbe@hellmann.net>  
  
RUN pip install awscli --ignore-installed six  
  
ENV aws_access_key_id YOUR_ACCESS_KEY_ID_HERE  
ENV aws_secret_access_key YOUR_SECRET_ACCESS_KEY_HERE  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["$aws_access_key_id $aws_secret_access_key eu-west-1"]  

