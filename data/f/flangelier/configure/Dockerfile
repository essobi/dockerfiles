FROM python:2.7-slim  
  
MAINTAINER Francois Langelier <f.langelier@gmail.com>  
  
VOLUME /kafka  
  
ADD configure.py .  
  
ENTRYPOINT ["./configure.py"]  
CMD -h

