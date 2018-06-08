# inherit from this image  
FROM slafs/sentry  
  
# install your extra dependencies e.g. sentry-github  
# (there are some dependency issues with redis)  
RUN pip install mysql-python  
RUN pip install django-smtp-ssl  
RUN pip install sentry-jira  

