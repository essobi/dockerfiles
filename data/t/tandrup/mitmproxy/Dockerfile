FROM python:2.7  
MAINTAINER Mads M. Tandrup <mads@maetzke-tandrup.dk>  
  
RUN pip install mitmproxy && rm -Rf ~/.cache/pip /tmp/pip_build_root  
  
EXPOSE 8080  
VOLUME /ca  
  
CMD mitmproxy --cadir /ca  

