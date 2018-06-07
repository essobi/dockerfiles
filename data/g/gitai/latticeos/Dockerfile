FROM python:2.7-alpine  
MAINTAINER Francesco Uliana <francesco@uliana.it>  
  
RUN pip install docker-compose  
  
COPY . /lattice  
  
ENTRYPOINT [ "/lattice/start.sh"]

