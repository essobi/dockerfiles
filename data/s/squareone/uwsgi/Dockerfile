FROM python:3.4  
RUN apt-get update && \  
pip3 install uwsgi==2.0.10 && \  
rm -rf /var/lib/apt/lists/*  
  
  
VOLUME [/var/run/uwsgi]  
WORKDIR /srv/app  
CMD ["uwsgi", "--ini", "/srv/app/uwsgi.ini"]

