FROM sentry:8  
RUN sed -i "s/^SENTRY_WEB_PORT = 9000/SENTRY_WEB_PORT = env('SENTRY_WEB_PORT')
or 9000/" /etc/sentry/sentry.conf.py  
  
COPY ./another_entrypoint.sh /another_entrypoint.sh  
  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
ENTRYPOINT ["/another_entrypoint.sh"]  

