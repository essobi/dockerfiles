FROM sentry:8.7-onbuild  
RUN apt-get update -y  
RUN apt-get install -y netcat  
  
RUN pip install sentry-slack  
RUN chmod a+x /usr/src/sentry/*.sh  
  
RUN pip install gevent gunicorn  

