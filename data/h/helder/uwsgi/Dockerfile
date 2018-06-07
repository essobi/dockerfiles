FROM python:2.7  
MAINTAINER Helder Correia <me@heldercorreia.com>  
  
# install uwsgi  
RUN pip install uwsgi uwsgitop  
COPY uwsgi.ini /etc/  
  
# run in /usr/src/app  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# expose uwsgi socket and stats ports  
EXPOSE 9000 3000  
# run uwsgi  
CMD ["uwsgi", "/etc/uwsgi.ini"]  

