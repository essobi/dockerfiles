FROM python:3.5  
  
RUN apt-get update \  
&& apt-get install -y ghostscript \  
&& rm -rf /var/cache/apt  
  
RUN pip install --no-cache-dir tox coverage  

