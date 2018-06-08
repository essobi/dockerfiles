FROM sentry:7.7.0  
  
USER  root  
RUN pip install sentry-github sentry-slack django-redis gevent>=0.13 newrelic  
USER  user  
  
VOLUME ["/usr/local/lib/python2.7/site-packages/sentry/static"]  
ENTRYPOINT ["newrelic-admin", "run-program"]  

