FROM datadog/docker-dd-agent  
  
# Workaround for https://github.com/DataDog/dd-agent/issues/1342. Will be
removed after 5.2 is released.  
RUN sed -i 's/self._count_images(instance)/#self._count_images(instance)/g'
/opt/datadog-agent/agent/checks.d/docker.py  

