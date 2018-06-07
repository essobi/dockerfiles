FROM python:3.6  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libgdal1-dev \  
libgeos-dev \  
libspatialindex-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
  
# default - will be overridden in Heroku  
# https://devcenter.heroku.com/articles/container-registry-and-runtime#get-
the-port-from-the-environment-variable  
ENV PORT 8000  
EXPOSE ${PORT}  
CMD gunicorn --bind 0.0.0.0:$PORT app:app  

