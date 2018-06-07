FROM lucidfrontier45/python-uwsgi:3.6-alpine  
  
RUN adduser -S www-data && addgroup www-data && pip install paste pastedeploy
falcon  
  
ADD uwsgi.conf /etc  
  
ADD entry /  
  
VOLUME /var/www /run/uwsgi  
  
CMD /entry  

