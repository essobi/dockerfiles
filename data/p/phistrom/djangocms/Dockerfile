FROM python:3.6  
LABEL description="Django CMS Base Image for MySQL" version="3.4.5"  
  
# for django-compressor  
RUN apt-get update && apt-get install --no-install-recommends -y \  
closure-compiler \  
&& rm -rf /var/lib/apt/lists/*  
  
# install Django CMS and a lot of extra Django plugins like compressor,
storages, and redis  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm
/tmp/requirements.txt  

