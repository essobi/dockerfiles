FROM orbweb/python:2.7.10-slim  
MAINTAINER Orbweb Inc <devs@orbweb.com>  
  
RUN pip install flower==0.8.3 redis  
  
EXPOSE 5555  
ENTRYPOINT ["flower"]  
CMD ["--adress=0.0.0.0", "--port=5555"]  

