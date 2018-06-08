FROM python:2.7  
MAINTAINER Rob Haswell <me@robhaswell.co.uk>  
  
VOLUME /certs  
ENV CONTROL_SERVICE 127.0.0.1  
ENV CONTROL_PORT 4523  
RUN pip install git+https://github.com/clusterhq/unofficial-flocker-tools.git  
ENTRYPOINT ["/usr/local/bin/flocker-volumes", "--certs-path", "/certs", "--
control-service", "$CONTROL_SERVICE", "--control-port", "$CONTROL_PORT"]  

