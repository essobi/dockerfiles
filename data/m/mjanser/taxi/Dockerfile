FROM python:2  
MAINTAINER Martin Janser <martin@duss-janser.ch>  
  
RUN apt-get update && apt-get install -y git vim nano  
RUN pip install taxi==3.2.1  
  
ENTRYPOINT ["taxi"]  

