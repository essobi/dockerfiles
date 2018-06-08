FROM rhangelxs/sentry-docker:8.2  
RUN pip install sentry-slack  
RUN pip install sentry-jira  
RUN pip install sentry-ldap-auth  
  
ADD sentry_docker_ldapauth_conf.py /conf/  
  
ENV PYTHONPATH /conf  
ENV SENTRY_CONF_FILE /conf/sentry_docker_ldapauth_conf.py  
  
# expose the new port  
EXPOSE 9000  

