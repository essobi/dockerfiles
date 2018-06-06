FROM eeacms/python:2.7-slim  
  
# Copy code into image  
RUN mkdir live_catalogue  
COPY requirements.txt requirements-dev.txt requirements-dep.txt
/live_catalogue/  
WORKDIR live_catalogue  
  
# Install requirements  
RUN apt-get update -y\  
&& apt-get -y install --no-install-recommends cron \  
&& pip install -U setuptools \  
&& pip install -r requirements-dep.txt  
  
# Copy code  
COPY . /live_catalogue  
COPY live_catalogue/local_settings.py.docker live_catalogue/local_settings.py  
  
# Expose needed port  
EXPOSE 8002  
# Expose static volume  
VOLUME /live_catalogue/public/static/  
  
#Default command  
CMD ["./docker-entrypoint.sh"]  

