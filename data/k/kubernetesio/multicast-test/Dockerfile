FROM buildpack-deps:latest  
  
RUN apt-get update && apt-get -y install vim python-dev  
  
WORKDIR /  
COPY *.py /  
  
ENTRYPOINT ["/usr/bin/python"]  

