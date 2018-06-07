FROM datadog/docker-dd-agent  
  
# These need to be group writable so we can run as non root user.  
RUN chmod g+w /etc/dd-agent/datadog.conf  
RUN chmod g+w /var/log/datadog  
RUN chmod g+w /etc/dd-agent  
  
# Override entry point so we can force hostname to use `hostname` and  
# avoid requesting it from Docker. This is needed if do not want Docker  
# monitoring and only want dogstatd as sidecar container.  
COPY entrypoint.sh /entrypoint-dogstatsd.sh  
  
ENTRYPOINT [ "/entrypoint-dogstatsd.sh" ]  
  
USER 1001  

