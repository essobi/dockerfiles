from python:3  
RUN pip install errbot sleekxmpp pyasn1 pyasn1-modules  
  
# don't be root inside the container  
RUN adduser --disabled-password --gecos '' errbot  
USER errbot  
WORKDIR /home/errbot  
RUN mkdir -p /home/errbot/data /home/errbot/plugins  
  
ADD config.py /home/errbot/  
  
VOLUME ["/home/errbot/data", "/home/errbot/plugins"]  
CMD ["errbot"]  

