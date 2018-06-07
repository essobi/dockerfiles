FROM python:3.6  
ENV TERM vt100  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update &&\  
apt-get install -y\  
gdal-bin\  
gettext\  
gfortran\  
libatlas-base-dev\  
libblas-dev\  
liblapack-dev\  
netcat\  
net-tools\  
postgresql-client\  
zsh &&\  
apt-get clean  
  
COPY ./requirements /requirements  
  
RUN pip install -r /requirements/dev.txt\  
&& groupadd -r django\  
&& useradd -r -g django django  
  
COPY . /app  
RUN chown -R django /app  
  
COPY ./compose/entrypoint.sh /entrypoint.sh  
COPY ./compose/gunicorn.sh /gunicorn.sh  
  
RUN mkdir -p /var/run/celeryd  
RUN mkdir -p /var/log/celeryd  
  
COPY ./compose/workers /usr/local/bin/workers  
COPY ./compose/beat /usr/local/bin/beat  
  
RUN chown django /var/run/celeryd\  
&& chown django /var/log/celeryd  
  
WORKDIR /app  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/gunicorn.sh"]  

